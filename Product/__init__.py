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
