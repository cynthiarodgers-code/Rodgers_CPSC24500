"""
menu_item.py - Week 3 

The MenuItem class represents a single item on the coffee shop menu.

Attributes:
- name (str): drink name (e.g., "Latte")
- size (str): "Small", "Medium", or "Large"
- price (float): final price (base price + size upcharge)

Methods:
- __str__: returns a string like "Latte (Large) - $6.00"
"""


class MenuItem:

    def __init__(self, name, size, price, items):
        # TODO: store name, size, and price as instance attributes
        self.name = name
        self.size = size
        self.price = self.calculate_price() 
        self.items = items
        self.base_price = self.base_price
        
        
        items = [("Americano", "Small", 3.50),
        ("Cappucino", "Small", 4.25),
        ("Espresso", "Small",3.00),
        ("Latte", "Small", 4.75)]

        menu = [items]

        for items in menu:
            print(items)
    
    def calculate_price(self):
        upcharges = {"Small": 0.00, "Medium": 0.75, "Large": 1.25}
        size_upcharge = upcharges.get(self.size, 0.00)
        return self.base_price + size_upcharge


    def __str__(self):
        # TODO: return a string in the format "Latte (Large) - $6.00"
        # Hint: f"{self.name} ({self.size}) - ${self.price:.2f}"
        return (f"{self.name} ({self.size}) - ${self.price:.2f}")
            
    


    