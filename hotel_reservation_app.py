import pandas as pd

df = pd.read_csv("./app11/hotels.csv")


class Hotel:
    """Takes id input and checks if hotel has an available room and books a room for the user"""
    def __init__(self, hotel_id):
        pass

    def book_room(self):
        """Books a hotel room by changning its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Checks if hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability:
            return True
        else:
            return False


class ReservationTicket:
    """Generates reservation ticket with user's name at the available hotel"""
    def __init__(self, customer_name, hotel_object):
        pass

    def generate_ticket(self, name):
        pass


print(df)
hotel_id = input("Enter the ID of the hotel: ")
hotel = Hotel(hotel_id)
if hotel.available():
    hotel.book()
    user_name = input("Enter your name: ")
    reserve_ticket = ReservationTicket(name, hotel)
    print(reserve_ticket.generate_ticket())
else:
    print("No open space in this hotel.")