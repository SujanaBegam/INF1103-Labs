import json
from pathlib import Path

from product import PhysicalProduct, DigitalProduct
from inventory import Inventory 

DATA_FILE = Path(__file__).with_name("inventory.json")

def save_inventory(inventory):
    try:
        data = [
            product.to_dict()
            for product in inventory.get_products()
        ]

        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        print("Inventory saved successfully.")

    except OSError as error:
        print(f"Could not save inventory: {error}")

def load_inventory(inventory):
    if not DATA_FILE.exists():
        return

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            print("Invalid inventory file. Starting with empty inventory.")
            return

        for item in data:
            if not isinstance(item, dict):
                print("Skipping an invalid product record.")
                continue 

            try: 
                product_id = item["product_id"]
                name = item["name"]
                price = float(item["price"])
                stock = item["stock"]

                if (
                    not isinstance(product_id, str)
                    or not product_id.strip()
                    or not isinstance(name,str)
                    or not name.strip()
                    or isinstance(stock, bool)
                    or not isinstance(stock, int)
                    or stock < 0
                    or price < 0
                ):
                    raise ValueError("Invalid product information.")

                product_type = item["type"]

                if product_type == "physical":
                    weight = float(item[weight])

                    if weight < 0:
                        raise ValueError("Invalid weight.")

                    product = PhysicalProduct(
                        product_id, name, price, stock, weight
                    )

                elif product_type == "digital":
                    download_size = float(item["download_size"])

                    if download_size < 0:
                        raise ValueError("Invalid download size.")

                    product = DigitalProduct(
                        product_id, name, price, stock, download_size
                    )

                else:
                    raise ValueError("Unknown product type.")

                inventory.add_product(product)

            except (KeyError, TypeError, ValueError):
                print("Skipping an invalid product record.")

    except (OSError, json.JSONDecodeError):
        print("Could not read inventory.json. Starting with empty inventory.")

def get_non_empty_text(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value 

        print("This field cannot be empty.")

def get_non_negative_int(prompt):
    while True:
        value = input(prompt).strip()

        try:
            number = int(value)

            if number >= 0:
                return number 

            print("Please enter zero or positive number.")

        except ValueError:
            print("Please enter a valid whole number.")

def get_non_negative_float(prompt):
    while True: 
        value = input(prompt).strip()

        try: 
            number = float(value)

            if number >= 0:
                return number 

            print("Please enter zero or a positive number.")

        except ValueError:
            print("Please enter a valid number.")

def add_product_menu(inventory):
    print("\n--- Add Product ---")

    product_id = get_non_empty_text("Enter product ID: ")

    if inventory.search_product(product_id) is not None: 
        print("A product with this ID already exists.")
        return

    name = get_non_empty_text("Enter product name: ")
    price = get_non_negative_float("Enter product price: $")
    stock = get_non_negative_int("Enter stock quantity: ")

    print("\nSelect Product Type:")
    print("1. Physical Product")
    print("2. Digital Product")

    while True: 
        product_type = input("Enter product type (1-2): ").strip()

        if product_type == "1":
            weight = get_non_negative_float("Enter product weight (kg): ")
            product = PhysicalProduct(product_id, name, price, stock, weight)
            break

        elif product_type == "2":
            download_size = get_non_negative_float("Enter download size (MB): ")
            product = DigitalProduct(product_id, name, price, stock, download_size)
            break

        else:
            print("Invalid choice. Please enter 1 or 2.")

    inventory.add_product(product)

def update_stock_menu(inventory):
    print("\n--- Update Stock ---")

    product_id = get_non_empty_text("Enter product ID: ")
    product = inventory.search_product(product_id)

    if product is None: 
        print("Product not found.")
        return
    print(f"Current stock: {product.stock}")
    quantity = get_non_negative_int("Enter new stock quantity: ")

    if inventory.update_product_stock(product_id, quantity):
        print("\n--- Search Product ---")

        product_id = get_non_empty_text("Enter product ID: ")
        product = inventory.search_product(product_id)

        if product is None:
            print("Product not found.")
        else:
            product.display_information()

def search_product_menu(inventory):
    print("\n--- Search Product ---")

    product_id = get_non_empty_text("Enter product ID: ")
    product = inventory.search_product(product_id)

    if product is None:
        print("Product not found.")
    else:
        product.display_information()

def main(): 
    inventory = Inventory()
    load_inventory(inventory)

    while True: 
        print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
        print("1. Display all products")
        print("2. Add a product")
        print("3. Update stock")
        print("4. Search for a product")
        print("5. Save inventory")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            inventory.display_all()

        elif choice == "2":
            add_product_menu(inventory)

        elif choice == "3":
            update_stock_menu(inventory)

        elif choice == "4":
            search_product_menu(inventory)

        elif choice == "5":
            save_inventory(inventory)

        elif choice == "6":
            save_inventory(inventory)
            print("Thank you for using our Inventory Management System.")
            break

if __name__ == "__main__":
    main()

 
