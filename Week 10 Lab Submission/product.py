from abc import ABC, abstractmethod
from supplier import Supplier

class Product(ABC):
    def __init__(
            self, 
            product_id: str,
            name: str, 
            price: float, 
            stock: int, 
            supplier: Supplier
    ) -> None:
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock
        self.supplier: Supplier = supplier

    @property
    def product_id(self) -> str:
        return self.__product_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> float:
        return self.__price

    @property
    def stock(self) -> int:
        return self.__stock

    def update_stock(self, quantity: int) -> bool:
        if quantity < 0:
            print("Stock cannot be negative.")
            return False

        self.__stock = quantity
        return True

    def display_information(self) -> None:
        print(f"Product ID: {self.__product_id}")
        print(f"Name: {self.__name}")
        print(f"Price: {self.__price}")
        print(f"Stock: {self.__stock}")
        print(f"Supplier: {self.supplier.name}")

    def display_supplier_information(self) -> None:
        self.supplier.display_information()

    def to_dict(self) -> dict:
        return{
            "product_id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
            "supplier": self.supplier.to_dict()
        }

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        pass 

class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self) -> float:
        pass

class PhysicalProduct(Product, CanBeShipped):
    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        weight: float,
        supplier: Supplier
    ) -> None:
        super().__init__(
            product_id, name, price, stock, supplier
        )
        self.__weight = weight

    @property
    def weight(self) -> float:
        return self.__weight

    def display_information(self) -> None:
        super().display_information()
        print(f"Weight: {self.__weight} kg")
        print(self.get_fulfilment_info())

    def get_fulfilment_info(self) -> str:
        return "This product requires physical shipping."

    def calculate_shipping_cost(self) -> float:
        return self.__weight * 5

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["type"] = "physical"
        data["weight"] = self.__weight
        return data

class DigitalProduct(Product):
    def __init__(
            self, 
            product_id: str,
            name: str,
            price: float,
            stock: int,
            download_size: float,
            supplier: Supplier
    ) -> None:
        super().__init__(
            product_id, name, price, stock, supplier
        )
        self.__download_size = download_size

    @property
    def download_size(self) -> float:
        return self.__download_size

    def display_information(self) -> None:
        super().display_information()
        print(f"Download Size: {self.__download_size} MB")
        print(self.get_fulfilment_info())

    def get_fulfilment_info(self) -> str:
        return "This product is delivered digitally."

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["type"] = "digital"
        data["download_size"] = self.__download_size
        return data
    