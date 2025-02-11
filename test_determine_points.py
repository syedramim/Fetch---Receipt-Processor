import unittest
from data import Data, DataError
from determine_points import ReceiptPoints, ReceiptPointsError
from ReceiptModel import Receipt, Item

class TestReceiptProcessor(unittest.TestCase):
    def setUp(self):
        self.points_calculator = ReceiptPoints()
        self.data_storage = Data()

    def test_target_receipt_points(self):
        r = Receipt(
            retailer="Target",
            purchaseDate="2022-01-01",
            purchaseTime="13:01",
            items=[
                Item(shortDescription="Mountain Dew 12PK", price="6.49"),
                Item(shortDescription="Emils Cheese Pizza", price="12.25"),
                Item(shortDescription="Knorr Creamy Chicken", price="1.26"),
                Item(shortDescription="Doritos Nacho Cheese", price="3.35"),
                Item(shortDescription="   Klarbrunn 12-PK 12 FL OZ  ", price="12.00")
            ],
            total="35.35"
        )
        pts = self.points_calculator.get_points(r.model_dump())
        self.assertEqual(pts, 28)

    def test_m_and_m_corner_market_points(self):
        r = Receipt(
            retailer="M&M Corner Market",
            purchaseDate="2022-03-20",
            purchaseTime="14:33",
            items=[
                Item(shortDescription="Gatorade", price="2.25"),
                Item(shortDescription="Gatorade", price="2.25"),
                Item(shortDescription="Gatorade", price="2.25"),
                Item(shortDescription="Gatorade", price="2.25")
            ],
            total="9.00"
        )
        pts = self.points_calculator.get_points(r.model_dump())
        self.assertEqual(pts, 109)

    def test_add_and_retrieve_data(self):
        r = Receipt(
            retailer="Store",
            purchaseDate="2022-01-02",
            purchaseTime="15:01",
            items=[Item(shortDescription="Test", price="1.00")],
            total="1.00"
        )
        record_id = self.data_storage.add_data(r)
        retrieved = self.data_storage.get_data_by_id(record_id)
        self.assertEqual(retrieved, r)

    def test_data_error_when_not_found(self):
        with self.assertRaises(DataError):
            self.data_storage.get_data_by_id("invalid_id")

    def test_receipt_points_error(self):
        invalid = {
            "retailer": "",
            "purchaseDate": "2022-01-02",
            "purchaseTime": "15:01",
            "items": [],
            "total": ""
        }
        with self.assertRaises(ReceiptPointsError):
            self.points_calculator.get_points(invalid)

if __name__ == "__main__":
    unittest.main()
