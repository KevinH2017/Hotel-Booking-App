import pandas as pd

df = pd.read_csv("./app11/hotels.csv", dtype={"id":str})
df_cards = pd.read_csv("./app11/cards.csv", dtype=str).to_dict(orient="records")
df_card_security = pd.read_csv("./app11/card_security.csv", dtype=str)

class Hotel:
    """Takes id input and checks if hotel has an available room and books a room for the user"""
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book_room(self):
        """Books a hotel room by changning its availability to 'no'"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("./app11/hotels.csv", index=False)

    def available(self):
        """Checks if hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False


class SpaHotel(Hotel):
    def book_spa_package(self):
        pass

    
class ReservationTicket:
    """Generates reservation ticket with user's name with the available hotel"""
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate_ticket(self):
        """Creates ticket for customer_name with hotel_object"""
        ticket_text = f"""
        Thank you for your reservation!
        Here is your hotel booking data:
        Name: {self.customer_name}
        Hotel: {self.hotel.name}
        Enjoy your stay!
        """
        return ticket_text


class CreditCardInfo:
    """Checks credit card information inputted in credit_card.validate() against cards.csv"""
    def __init__(self, num):
        self.num = num

    def validate(self, expiration, holder, cvc):
        """Returns True or False against card_data to df_cards csv file"""
        card_data = {"number":self.num, "expiration":expiration, "holder":holder, "cvc":cvc}
        if card_data in df_cards:
            return True
        else:
            return False


class CardSecurity(CreditCardInfo):
    """Child class that inherits Parent class CreditCardInfo methods"""
    def authenticate(self, input_password):
        """Authenticates if the credit card number matches its password"""
        password = df_card_security.loc[df_card_security["number"] == self.num, "password"].squeeze()
        if password == input_password:
            return True
        else:
            return False

class SpaTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def spa_message(self):
        content = f"""
        Thank you for your SPA reservation!
        Here is your SPA booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name}
        """
        return content


print(df)
hotel_id = input("Enter the ID of the hotel: ")
hotel = SpaHotel(hotel_id)
if hotel.available():
    input_cc_num = input("Input Credit Card #: ")
    input_password = input("Input Credit Card Password: ")
    input_holder_name = input("Enter Holder Name: ")
    input_cvc = input("Enter CVC #: ")
    input_expiration = input("Enter Expiration Date: ")
    credit_card = CardSecurity(num=input_cc_num)
    
    if credit_card.validate(expiration=input_expiration, holder=input_holder_name, cvc=input_cvc):
        if credit_card.authenticate(input_password=input_password):
            hotel.book_room()
            user_name = input("Enter your name: ")
            reserve_ticket = ReservationTicket(customer_name=user_name, hotel_object=hotel)
            print(reserve_ticket.generate_ticket())
            spa_package = input("Do you want to book a spa package? ")
            if spa_package == "yes":
                hotel.book_spa_package()
                spa_booking = SpaTicket(customer_name=name, hotel_object=hotel)
                print(spa_booking.spa_message())
            else:
                pass
        else:
            print("ERROR! Incorrect Password!")
    else:
        print("ERROR! There was a problem with your payment!")
else:
    print("No space available in this hotel.")