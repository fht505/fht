from store import ORDERS


def orders_for_customer(customer):
    """All orders belonging to `customer`."""
    rows = []
    for order in ORDERS:
        if order["customer_id"] == customer["id"]:
            rows.append(order)
    return rows
