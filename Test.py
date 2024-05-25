import unittest
from Product import Product
from Store import Store


# help(unittest)
class TestProductStore(unittest.TestCase):
    def setUp(self):
        self.store = Store()
        self.store.add_product(Product('Mangue', 1200, 4))

    def test_get_product_price(self):
        self.assertEqual(self.store.get_product_price('Mangue'), 1200)

    def test_sell_product(self):
        self.assertTrue(self.store.sell_product('Mangue', 5))
        self.assertFalse(self.store.sell_product('Mangue', 11), 'Oops la valeur doit etre superieur a 4')

    def test_remove_product(self):
        self.store.remove_product('Mangue')
        self.assertNotIn('Mangue', [p for p in self.store.products])


if __name__ == "__main__":
    unittest.main()
