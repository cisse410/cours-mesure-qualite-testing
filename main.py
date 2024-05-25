# This is a sample Python script.
import unittest


# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Product:
    """
        Cette classe represente un produit
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initialise un nouveau produit avec un nom, un prix et une quantite
        :param name: str (Le nom du produit)
        :param price: float (Le prix du produit)
        :param quantity: int (La quantite du produit)
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_name(self):
        """
        Revoie le nom du produit
        :return: str (Le nom du produit)
        """
        return self.name

    def get_price(self):
        """
        Renvoie le prix du produit
        :return: float (Le prix du produit)
        """
        return self.price

    def get_quantity(self):
        """
        Renvoie la quantite du produit
        :return: int (La quantite du produit)
        """
        return self.quantity

    def set_quantity(self, quantity: int):
        """
        Definie la quantite du produit
        :param: float (La quantite du produit)
        """
        self.quantity = quantity


class Store:
    """
        Cette classe represente un store (magasin)
    """

    def __init__(self):
        """
            Initialise un avec une liste de produit vide
        """
        self.products = []

    def add_product(self, product: Product):
        """
        Ajoute un produit dans l'inventaire de la liste des produits
        :param product:
        """
        self.products.append(product)

    def remove_product(self, name: str):
        """
        Supprime un produit de l'inventaire d'un produit
        :param name: Nom du produit à supprimer.
        """
        self.products = [p for p in self.products if p.name != name]

    def update_product(self, name: str, new_quantity: int):
        """
        Modifie le prix et la quantité d'un produit.
        :param name: Nom du produit à modifier.
        :param new_quantity: Nouvelle quantité du produit.
        :return: True si la modification a réussi, False sinon.
        """
        for product in self.products:
            if product.name == name:
                product.quantity = new_quantity
                return True
        return False

    def get_available_products(self):
        """
        Renvoie la liste des produits disponibles dans le magasin.
        :return: Liste des produits (objets de la classe Product).
        """
        return self.products

    def get_total_stock_value(self):
        """
        Calcule la somme des prix des produits.
        :return: Valeur totale du stock (nombre à virgule flottante).
        """
        total_value = sum(product.price * product.quantity for product in self.products)
        return total_value


class TestProductStore(unittest.TestCase):
    def setUp(self):
        self.store = Store()
        self.store.add_product(Product('Mangue', 1200, 4))

    def test_remove_product(self):
        self.store.remove_product('Mangue')
        self.assertNotIn('Mangue', [p for p in self.store.products])


if __name__ == "__main__":
    unittest.main()
