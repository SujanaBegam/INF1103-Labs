
from product import Product


class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        if self.search_product(product.product_id) is not None:
            print("A product with this ID already exists.")
            return False

        self.__products.append(product)
        print("Product added successfully.")
        return True

    def search_product(self, product_id):
        for product in self.__products:
            if product.product_id.lower() == product_id.lower():
                return product

        return None

    def display_all(self):
        if not self.__products:
            print("Inventory is empty.")
            return

        for product in self.__products:
            print("-" * 30)
            product.display_information()

    def update_product_stock(self, product_id, quantity):
        product = self.search_product(product_id)

        if product is None:
            print("Product not found.")
            return False

        return product.update_stock(quantity)

    def get_products(self):
        return self.__products.copy()
