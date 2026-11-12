
from product import Product

class Inventory:
    def __init__(self) -> None:
        self.products: list[Product] = []

    def add_product(self, product: Product) -> None:
        self.products.append(product)
        print("Product added successfully.")

    def remove_product(self, product_id: str) -> None:
        product = self.find_product(product_id)

        if product is not None:
            self.products.remove(product)
            print("Product removed from inventory.")
        else:
            print("Product not found.")

    def find_product(self, product_id: str) -> Product | None:
        for product in self.products:
            if product.product_id == product_id:
                return product

            return None

    def search_product(self, product_id: str) -> Product | None:
            return self.find_product(product_id)

    def update_product_stock(
            self, product_id: str, quantity: int
    ) -> bool:
        product = self.find_product(product_id)

        if product is None:
            return False

        return product.update_stock(quantity)
    
    def display_all_products(self) -> None:
        if not self.products:
            print("Inventory is empty.")
            return

        print("\n===== ALL PRODUCTS =====")

        for product in self.products:
            print("--------------------")
            product.display_information()

    def display_all(self) -> None:
        self.display_all_products()

    def get_products(self) -> list[Product]:
        return self.products
