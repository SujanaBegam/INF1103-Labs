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
    return amount * 0.09 

def generate_report(total_units, failed_entries):
    print("Total Units Processed:", total_units)
    print("Failed/Rejected Entries:", failed_entries)

inventory = 0
failed_entries = 0
deliveries_processed = 0

while True:
    quantity = get_valid_input()

    if quantity == "quit":
        break

    if quantity is None:
        failed_entries += 1
        continue

    inventory = process_delivery(inventory, quantity)

    tax = calculate_tax(inventory)

    deliveries_processed += 1

    print("Total Tax:", tax)

    if inventory > 500:
        print("OVERSTOCK ALERT!: Inventory exceeds 500 units.")
        break

def generate_report(total_units, deliveries_processed, failed_attempts):
    print("Total Units Processed:", total_units)
    print("Total Deliveries Processed:", deliveries_processed)
    print("Failed/Rejected Entries:", failed_attempts)

generate_report(inventory, deliveries_processed, failed_entries)
