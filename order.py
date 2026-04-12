"""
order.py - Week 3

The Order class represents a customer's order containing one or more MenuItems.

Attributes:
- customer_name (str)
- items (list of MenuItem)

Methods:
- add_item(item): append a MenuItem to the order
- remove_item(index): remove an item by 1-based index
- subtotal(): sum of all item prices
- tax(): subtotal * 0.0875
- total(): subtotal + tax
- __str__: formatted receipt string
"""

from menu_item import MenuItem

TAX_RATE = 0.0875


class Order:

    def __init__(self, customer_name, items=None):
        # TODO: store the customer name
        # TODO: initialize an empty list for items
        self.customer_name = customer_name
        if items is None:
            self.items = []
        else:
            self.items = items

    def add_item(self, item):
        # TODO: append the item to self.items
        self.items.append(item)

    def remove_item(self, index):
        # TODO: remove the item at position (index - 1) since the menu shows 1-based numbers
        # Hint: use self.items.pop(index - 1)
        if 1 <= index <= len(self.items):
            self.items.pop(index - 1)

    def subtotal(self):
        # TODO: return the sum of prices for all items
        return sum(item.price for item in self.items)

    def tax(self):
        # TODO: return self.subtotal() * TAX_RATE
        return self.subtotal() * 0.0875

    def total(self):
        # TODO: return subtotal + tax
        return self.subtotal() + self.tax()

    def __str__(self):
        # TODO: build and return a formatted receipt string
        # Include: header, customer name, each item with number, subtotal, tax, total
        receipt = f"Customer: {self.customer_name}\n"
        receipt += "------------------------------\n"
        for i, item in enumerate(self.items, 1):
            receipt += f"{i}. {item}\n"
        receipt += "------------------------------\n"
        receipt += f"Subtotal: ${self.subtotal():.2f}\n"
        receipt += f"Tax (8.75%): ${self.tax():.2f}\n"
        receipt += f"Total: ${self.total():.2f}\n"
        return receipt