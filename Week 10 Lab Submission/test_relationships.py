
from supplier import Supplier
from product import Product, PhysicalProduct, DigitalProduct
from inventory import Inventory
from order import Order


def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())


def main() -> None:
    supplier = Supplier(
        "S001", "Test Supplier", "test@example.com"
    )

    physical = PhysicalProduct(
        "P001", "Laptop", 1200.0, 10, 2.5, supplier
    )

    digital = DigitalProduct(
        "D001", "Python Course", 50.0, 100, 500.0, supplier
    )

    print("\n=== ASSOCIATION ===")
    physical.display_supplier_information()
    digital.display_supplier_information()

    del supplier
    print("Supplier variable deleted.")
    physical.display_supplier_information()

    print("\n=== AGGREGATION ===")
    inventory_a = Inventory()
    inventory_b = Inventory()

    inventory_a.add_product(physical)
    inventory_a.remove_product("P001")

    print("Product still exists:")
    physical.display_information()

    inventory_b.add_product(physical)
    assert inventory_b.find_product("P001") is physical

    print("\n=== COMPOSITION ===")
    order1 = Order("O001")
    order1.add_order_line(physical, 2)
    order1.add_order_line(digital, 1)
    order1.display_order()

    order2 = Order("O002")
    order2.add_order_line(physical, 1)

    assert order1.order_lines[0] is not order2.order_lines[0]
    assert order1.order_lines[0].product is physical
    assert order2.order_lines[0].product is physical

    print("\n=== LSP AND POLYMORPHISM ===")
    inventory_b.add_product(digital)

    for product in inventory_b.get_products():
        show_product_details(product)

    assert physical.update_stock(5)
    assert digital.update_stock(20)

    print("\nAll relationship tests passed.")


if __name__ == "__main__":
    main()
