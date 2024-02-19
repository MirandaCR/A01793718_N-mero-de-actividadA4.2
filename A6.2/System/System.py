from hotel_management import HotelManager, CustomerManager, ReservationManager, Hotel, Customer, Reservation

def create_hotel():
    name = input("Enter hotel name: ")
    location = input("Enter hotel location: ")
    rooms = int(input("Enter number of rooms: "))
    hotel = Hotel(name, location, rooms)
    hotel_manager.create_hotel(hotel)
    print("Hotel created successfully.")

def delete_hotel():
    name = input("Enter hotel name to delete: ")
    hotel_manager.delete_hotel(name)
    print("Hotel deleted successfully.")

def display_hotel_info():
    name = input("Enter hotel name to display information: ")
    hotel_manager.display_hotel_info(name)

def modify_hotel_info():
    name = input("Enter hotel name to modify information: ")
    new_name = input("Enter new hotel name (leave empty to keep current): ")
    new_location = input("Enter new location (leave empty to keep current): ")
    new_rooms = input("Enter new number of rooms (leave empty to keep current): ")
    
    current_info = hotel_manager.get_hotel_data().get(name)
    if current_info is None:
        print("Hotel not found.")
        return
    
    new_info = {
        "name": new_name if new_name else current_info.get("name"),
        "location": new_location if new_location else current_info.get("location"),
        "rooms": int(new_rooms) if new_rooms else current_info.get("rooms")
    }
    hotel_manager.modify_hotel_info(name, new_info)
    print("Hotel information modified successfully.")

def create_customer():
    name = input("Enter customer name: ")
    email = input("Enter customer email: ")
    customer = Customer(name, email)
    customer_manager.create_customer(customer)
    print("Customer created successfully.")

def delete_customer():
    name = input("Enter customer name to delete: ")
    customer_manager.delete_customer(name)
    print("Customer deleted successfully.")

def display_customer_info():
    name = input("Enter customer name to display information: ")
    customer_manager.display_customer_info(name)

def modify_customer_info():
    name = input("Enter customer name to modify information: ")
    new_name = input("Enter new customer name (leave empty to keep current): ")
    new_email = input("Enter new email (leave empty to keep current): ")
    
    current_info = customer_manager.get_customer_data().get(name)
    if current_info is None:
        print("Customer not found.")
        return
    
    new_info = {
        "name": new_name if new_name else current_info.get("name"),
        "email": new_email if new_email else current_info.get("email")
    }
    customer_manager.modify_customer_info(name, new_info)
    print("Customer information modified successfully.")

def create_reservation():
    customer_name = input("Enter customer name: ")
    hotel_name = input("Enter hotel name: ")
    reservation = Reservation(customer_name, hotel_name)
    reservation_manager.create_reservation(reservation)
    print("Reservation created successfully.")

def cancel_reservation():
    customer_name = input("Enter customer name: ")
    hotel_name = input("Enter hotel name: ")
    reservation_manager.cancel_reservation(customer_name, hotel_name)
    print("Reservation canceled successfully.")

def display_menu():
    print("\nMenu:")
    print("1. Create Hotel")
    print("2. Delete Hotel")
    print("3. Display Hotel Information")
    print("4. Modify Hotel Information")
    print("5. Create Customer")
    print("6. Delete Customer")
    print("7. Display Customer Information")
    print("8. Modify Customer Information")
    print("9. Create Reservation")
    print("10. Cancel Reservation")
    print("0. Exit")

hotel_manager = HotelManager("hotels.json")
customer_manager = CustomerManager("customers.json")
reservation_manager = ReservationManager("reservations.json")

while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        create_hotel()
    elif choice == "2":
        delete_hotel()
    elif choice == "3":
        display_hotel_info()
    elif choice == "4":
        modify_hotel_info()
    elif choice == "5":
        create_customer()
    elif choice == "6":
        delete_customer()
    elif choice == "7":
        display_customer_info()
    elif choice == "8":
        modify_customer_info()
    elif choice == "9":
        create_reservation()
    elif choice == "10":
        cancel_reservation()
    elif choice == "0":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
