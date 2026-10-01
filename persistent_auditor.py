def load_inventory():
    try:
        with open("inventory.txt", "r") as file:
            lines = file.readlines()

            total = int(lines[0].strip().replace("Total: ", ""))

            transactions_text = lines[1].strip().replace("Transactions: ", "")

            transactions = eval(transactions_text)

            return total, transactions

    except FileNotFoundError:
        return 0, []

def save_inventory(total, transactions):
    with open("inventory.txt", "w") as file:
        file.write("Total: " + str(total) + "\n")
        file.write("Transactions: " + str(transactions) + "\n")

def get_valid_input():
    quantity = input("Enter stock quantity: ")

    if quantity == "quit":
        return "quit"

    if not quantity.isdigit():
        print("Invalid input")
        return None

    return int(quantity)

def process_delivery(current_total, new_value):
    return current_total + new_value

def calculate_tax(amount):
    return round(amount * 0.09, 2)

def generate_report(total_units, deliveries_processed, failed_attempts):
    print("Total Units Processed:", total_units)
    print("Total Deliveries Processed:", deliveries_processed)
    print("Failed/Rejected Entries:", failed_attempts)

inventory, transaction_history = load_inventory()

failed_entries = 0
deliveries_processed = 0

print("Current Inventory:", inventory)
print("Transaction History:", transaction_history)

while True:
    quantity = get_valid_input()

    if quantity == "quit":
        save_inventory(inventory, transaction_history)
        print("Inventory successfully saved to inventory.txt")
        break

    if quantity is None:
        failed_entries += 1
        continue

    inventory = process_delivery(inventory, quantity)

    transaction_history.append(quantity)

    tax = calculate_tax(inventory)

    deliveries_processed += 1

    print("Total Tax:", tax)

generate_report(inventory, deliveries_processed, failed_entries)
