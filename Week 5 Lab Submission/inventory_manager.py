import json
import os


# ========================================
# LOAD INVENTORY
# ========================================

def load_inventory():
    """Load inventory from inventory.json if it exists."""

    if os.path.exists("inventory.json"):
        print("inventory.json found.")

        with open("inventory.json", "r") as file:
            inventory = json.load(file)

        print("Inventory loaded successfully.")
        return inventory

    else:
        print("inventory.json not found.")
        print("Starting with empty inventory.")
        return []


# ========================================
# SAVE INVENTORY
# ========================================

def save_inventory(inventory):
    """Save inventory to inventory.json."""

    with open("inventory.json", "w") as file:
        json.dump(inventory, file, indent=4)

    print("Inventory saved successfully to inventory.json.")


# ========================================
# DISPLAY ALL PRODUCTS
# ========================================

def display_all(inventory):
    """Display all products in the inventory."""

    if len(inventory) == 0:
        print("Inventory is empty.")
        return

    print("\nCurrent Inventory")
    print("-" * 48)

    for product in inventory:
        print(
            f"ID: {product['id']} | "
            f"Name: {product['name']} | "
            f"Price: ${product['price']:.2f} | "
            f"Stock: {product['stock']}"
        )

    print("-" * 48)


# ========================================
# ADD PRODUCT
# ========================================

def add_product(inventory):
    """Add a new product to the inventory."""

    print("\nAdd New Product")

    product_id = input("Product ID: ").strip()

    # Check if product ID already exists
    for product in inventory:
        if product["id"] == product_id:
            print("Product ID already exists.")
            return

    product_name = input("Product Name: ").strip()

    # Validate price
    while True:
        try:
            price = float(input("Price: "))

            if price < 0:
                print("Price cannot be negative.")
            else:
                break

        except ValueError:
            print("Please enter a valid number.")

    # Validate stock
    while True:
        try:
            stock = int(input("Stock Quantity: "))

            if stock < 0:
                print("Stock cannot be negative.")
            else:
                break

        except ValueError:
            print("Please enter a whole number.")

    # Create product dictionary
    product = {
        "id": product_id,
        "name": product_name,
        "price": price,
        "stock": stock
    }

    # Add dictionary to list
    inventory.append(product)

    print("\nProduct added successfully!")


# ========================================
# UPDATE STOCK
# ========================================

def update_stock(inventory):
    """Update the stock quantity of an existing product."""

    print("\nUpdate Stock")

    product_id = input("Enter Product ID: ").strip()

    # Search for product
    for product in inventory:

        if product["id"] == product_id:

            print("\nProduct Found:")
            print(f"Name: {product['name']}")
            print(f"Current Stock: {product['stock']}")

            # Get new stock
            while True:
                try:
                    new_stock = int(input("\nNew Stock Quantity: "))

                    if new_stock < 0:
                        print("Stock cannot be negative.")
                    else:
                        break

                except ValueError:
                    print("Please enter a whole number.")

            product["stock"] = new_stock

            print("\nStock updated successfully!")
            return

    print("Product not found.")


# ========================================
# SEARCH PRODUCT
# ========================================

def search_product(inventory):
    """Search for a product using its ID."""

    print("\nSearch Product")

    product_id = input("Enter Product ID: ").strip()

    # Search through inventory
    for product in inventory:

        if product["id"] == product_id:

            print("\nProduct Found")
            print("-" * 48)
            print(f"ID: {product['id']}")
            print(f"Name: {product['name']}")
            print(f"Price: ${product['price']:.2f}")
            print(f"Stock: {product['stock']}")
            print("-" * 48)

            return

    print("\nProduct not found.")


# ========================================
# MENU
# ========================================

def display_menu():
    """Display the menu options."""

    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")


# ========================================
# MAIN PROGRAM
# ========================================

def main():

    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)

    # Load existing inventory
    inventory = load_inventory()

    # If no inventory exists, create 3 products
    if len(inventory) == 0:
        inventory = [
            {
                "id": "P001",
                "name": "Laptop",
                "price": 1200.00,
                "stock": 15
            },
            {
                "id": "P002",
                "name": "Mouse",
                "price": 25.50,
                "stock": 40
            },
            {
                "id": "P003",
                "name": "Keyboard",
                "price": 45.00,
                "stock": 25
            }
        ]

    # Menu loop
    while True:

        display_menu()

        choice = input("\nEnter option: ").strip()

        if choice == "1":

            display_all(inventory)

        elif choice == "2":

            add_product(inventory)

        elif choice == "3":

            update_stock(inventory)

        elif choice == "4":

            search_product(inventory)

        elif choice == "5":

            print("\nSaving inventory...")
            save_inventory(inventory)

        elif choice == "6":

            print("\nSaving inventory before exit...")
            save_inventory(inventory)

            print("\nThank you for using Inventory Management System.")
            print("Program terminated.")

            break

        else:

            print("Invalid option. Please enter a number from 1 to 6.")


# ========================================
# RUN PROGRAM
# ========================================

if __name__ == "__main__":
    main()