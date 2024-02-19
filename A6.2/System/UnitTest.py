from hotel_management import Hotel, Customer, Reservation, HotelManager, CustomerManager, ReservationManager
import unittest
import os
from unittest.mock import patch
import tempfile

class TestHotelManager(unittest.TestCase):
    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)

    def tearDown(self):
        os.remove(self.temp_file.name)

    def test_load_data(self):
        with patch("builtins.open", return_value=self.temp_file) as mock_open:
            manager = HotelManager(self.temp_file.name)
            mock_open.assert_called_once_with(self.temp_file.name, "r", encoding="utf-8")

    def test_save_data(self):
        with patch("builtins.open", return_value=self.temp_file) as mock_open:
            manager = HotelManager(self.temp_file.name)
            manager.hotels = {"hotel1": {"name": "Hotel 1"}}
            manager.save_data()
            mock_open.assert_called_once_with(self.temp_file.name, "w", encoding="utf-8")
            self.assertEqual(self.temp_file.read(), b'{"hotel1": {"name": "Hotel 1"}}')

    def test_create_hotel(self):
        manager = HotelManager(self.temp_file.name)
        hotel = Hotel(name="Hotel 1", location="Location 1", rooms=10)
        manager.create_hotel(hotel)
        self.assertEqual(manager.hotels, {"Hotel 1": {"name": "Hotel 1", "location": "Location 1", "rooms": 10}})

    def test_delete_hotel(self):
        manager = HotelManager(self.temp_file.name)
        manager.hotels = {"Hotel 1": {"name": "Hotel 1", "location": "Location 1", "rooms": 10}}
        manager.delete_hotel("Hotel 1")
        self.assertEqual(manager.hotels, {})

    def test_display_hotel_info(self):
        manager = HotelManager(self.temp_file.name)
        manager.hotels = {"Hotel 1": {"name": "Hotel 1", "location": "Location 1", "rooms": 10}}
        with patch("builtins.print") as mocked_print:
            manager.display_hotel_info("Hotel 1")
            mocked_print.assert_called_once_with({"name": "Hotel 1", "location": "Location 1", "rooms": 10})

    def test_modify_hotel_info(self):
        manager = HotelManager(self.temp_file.name)
        manager.hotels = {"Hotel 1": {"name": "Hotel 1", "location": "Location 1", "rooms": 10}}
        manager.modify_hotel_info("Hotel 1", {"name": "New Name"})
        self.assertEqual(manager.hotels["Hotel 1"], {"name": "New Name"})

    def test_reserve_room(self):
        manager = HotelManager(self.temp_file.name)
        manager.hotels = {"Hotel 1": {"name": "Hotel 1"}}
        manager.reserve_room("Hotel 1", "Room 101")
        self.assertEqual(manager.hotels["Hotel 1"]["reservations"], ["Room 101"])

    def test_cancel_reservation(self):
        manager = HotelManager(self.temp_file.name)
        manager.hotels = {"Hotel 1": {"name": "Hotel 1", "reservations": ["Room 101"]}}
        manager.cancel_reservation("Hotel 1", "Room 101")
        self.assertEqual(manager.hotels["Hotel 1"]["reservations"], [])

    def test_get_hotel_data(self):
        manager = HotelManager(self.temp_file.name)
        manager.hotels = {"Hotel 1": {"name": "Hotel 1"}}
        self.assertEqual(manager.get_hotel_data(), {"Hotel 1": {"name": "Hotel 1"}})


if __name__ == "__main__":
    unittest.main()