from store import CUSTOMERS, ORDERS


def orders_for_customer(customer):
    """All orders belonging to `customer`."""
    rows = []
    for order in ORDERS:
        owner = next(c for c in CUSTOMERS if c["id"] == order["customer_id"])
        if owner["name"] == customer["name"]:
            rows.append(order)
    return rows
