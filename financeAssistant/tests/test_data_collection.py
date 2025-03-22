import unittest
from src.data_collection.market_data import get_stock_data

class TestMarketData(unittest.TestCase):
    def test_get_stock_data(self):
        data = get_stock_data("PETR4.SA")
        self.assertIsNotNone(data)

if __name__ == "__main__":
    unittest.main()