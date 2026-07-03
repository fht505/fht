from store import CUSTOMERS
from queries import orders_for_customer


def build_report():
    """One line per order: (customer email, order id, amount)."""
    lines = []
    for customer in CUSTOMERS:
        for order in orders_for_customer(customer):
            lines.append((customer["email"], order["order_id"], order["amount"]))
    return lines


def total_billed():
    return sum(amount for _, _, amount in build_report())
