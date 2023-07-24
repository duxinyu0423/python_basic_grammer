import unittest
from shopping_list import ShoppingList

class TestShoppingList(unittest.TestCase):
    def setUp(self):
        self.shopping_list = ShoppingList({'a':8, 'b':18, 'c':22, 'd':10})
        
    def test_get_item_count(self):
        self.assertEqual(self.shopping_list.get_items_count(), 4)

        
    def test_get_total_price2(self):
        self.assertEqual(self.shopping_list.get_total_price(), 57)