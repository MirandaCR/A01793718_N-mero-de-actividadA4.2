""" Modules """

import json
import os


class Hotel:
    """
    Represents a hotel.
    """
    def __init__(self, name, location, rooms):
        self.name = name
        self.location = location
        self.rooms = rooms

    def to_dict(self):
        """
        Convert hotel information to dictionary.
        """
        return {
            "name": self.name,
            "location": self.location,
            "rooms": self.rooms
        }

    def __repr__(self):
        return f"Hotel(name={self.name}, location={self.location}, rooms={self.rooms})"


class Reservation:
    """
    Represents a reservation.
    """
    def __init__(self, customer, hotel):
        self.customer = customer
        self.hotel = hotel

    def to_dict(self):
        """
        Convert reservation information to dictionary.
        """
        return {
            "customer": self.customer,
            "hotel": self.hotel
        }

    def __repr__(self):
        return f"Reservation(customer={self.customer}, hotel={self.hotel})"


class Customer:
    """
    Represents a customer.
    """
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def to_dict(self):
        """
        Convert customer information to dictionary.
        """
        return {
            "name": self.name,
            "email": self.email
        }

    def __repr__(self):
        return f"Customer(name={self.name}, email={self.email})"


class HotelManager:
    """
    Manager class for hotels.
    """
    def __init__(self, filename):
        self.filename = filename
        self.hotels = self.load_data()

    def load_data(self):
        """
        Load hotel data from file.
        """
        if not os.path.exists(self.filename):
            return {}
        with open(self.filename, "r", encoding="utf-8") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError as error:
                print(f"Error loading data from {self.filename}: {error}")
                return {}

    def save_data(self):
        """
        Save hotel data to file.
        """
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(self.hotels, file)
        file.close()

    def create_hotel(self, hotel):
        """
        Create a new hotel.
        """
        self.hotels[hotel.name] = hotel.to_dict()
        self.save_data()

    def delete_hotel(self, name):
        """
        Delete a hotel.
        """
        if name in self.hotels:
            del self.hotels[name]
            self.save_data()

    def display_hotel_info(self, name):
        """
        Display information about a hotel.
        """
        if name in self.hotels:
            print(self.hotels[name])
        else:
            print(f"Hotel '{name}' not found.")

    def modify_hotel_info(self, name, new_info):
        """
        Modify hotel information.
        """
        if name in self.hotels:
            self.hotels[name] = new_info
            self.save_data()
        else:
            print(f"Hotel '{name}' not found.")

    def reserve_room(self, hotel_name, room):
        """
        Reserve a room in a hotel.
        """
        if hotel_name in self.hotels:
            if "reservations" not in self.hotels[hotel_name]:
                self.hotels[hotel_name]["reservations"] = []
            self.hotels[hotel_name]["reservations"].append(room)
            self.save_data()
        else:
            print(f"Hotel '{hotel_name}' not found.")

    def cancel_reservation(self, hotel_name, room):
        """
        Cancel a room reservation.
        """
        if hotel_name in self.hotels and "reservations" in self.hotels[hotel_name]:
            if room in self.hotels[hotel_name]["reservations"]:
                self.hotels[hotel_name]["reservations"].remove(room)
                self.save_data()
            else:
                print(f"Room '{room}' is not reserved for '{hotel_name}'.")
        else:
            print(f"Hotel '{hotel_name}' not found or no reservations exist.")

    def get_hotel_data(self):
        """
        Get hotel data.
        """
        return self.hotels


class CustomerManager:
    """
    Manager class for customers.
    """
    def __init__(self, filename):
        self.filename = filename
        self.customers = self.load_data()

    def load_data(self):
        """
        Load customer data from file.
        """
        if not os.path.exists(self.filename):
            return {}
        with open(self.filename, "r", encoding="utf-8") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError as error:
                print(f"Error loading data from {self.filename}: {error}")
                return {}

    def save_data(self):
        """
        Save customer data to file.
        """
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(self.customers, file)

    def create_customer(self, customer):
        """
        Create a new customer.
        """
        self.customers[customer.name] = customer.to_dict()
        self.save_data()

    def delete_customer(self, name):
        """
        Delete a customer.
        """
        if name in self.customers:
            del self.customers[name]
            self.save_data()

    def display_customer_info(self, name):
        """
        Display information about a customer.
        """
        if name in self.customers:
            print(self.customers[name])
        else:
            print(f"Customer '{name}' not found.")

    def modify_customer_info(self, name, new_info):
        """
        Modify customer information.
        """
        if name in self.customers:
            self.customers[name] = new_info
            self.save_data()
        else:
            print(f"Customer '{name}' not found.")

    def get_customer_data(self):
        """
        Get customer data.
        """
        return self.customers


class ReservationManager:
    """
    Manager class for reservations.
    """
    def __init__(self, filename):
        self.filename = filename
        self.reservations = self.load_data()

    def load_data(self):
        """
        Load reservation data from file.
        """
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r", encoding="utf-8") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError as error:
                print(f"Error loading data from {self.filename}: {error}")
                return []

    def save_data(self):
        """
        Save reservation data to file.
        """
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(self.reservations, file)

    def create_reservation(self, reservation):
        """
        Create a new reservation.
        """
        self.reservations.append(reservation.to_dict())
        self.save_data()

    def cancel_reservation(self, customer, hotel):
        """
        Cancel a reservation.
        """
        self.reservations = [r for r in self.reservations if r["customer"] != customer or r["hotel"] != hotel]
        self.save_data()

    def get_reservation_data(self):
        """
        Get reservation data.
        """
        return self.reservations
