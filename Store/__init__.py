from Product import Product


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

    def get_product_price(self, name: str) -> float:
        """
        Renvoie le prix d'un produit par son nom.
        :param name: Nom du produit (chaîne de caractères).
        :return: Prix du produit (nombre à virgule flottante).
        """
        for product in self.products:
            if product.name == name:
                return product.price
        return 0.0  # Si le produit n'est pas trouvé, renvoie 0.0

    def sell_product(self, name: str, quantity: int):
        """
        Vente d'un produit par son nom et quantité.
        :param name: Nom du produit.
        :param quantity: Quantité vendue.
        :return: True si la vente a réussi, False sinon.
        """
        for product in self.products:
            if product.name == name:
                if product.quantity >= quantity:
                    product.quantity -= quantity
                    return True
                else:
                    return False
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
