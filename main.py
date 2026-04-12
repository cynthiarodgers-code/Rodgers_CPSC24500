"""
main.py - Week 3 

Menu-driven point-of-sale program.

Flow:
1. Welcome banner
2. Ask for customer name, create an Order
3. Show the drink menu, let the customer pick a drink and size
4. Build a MenuItem and add it to the order
5. Show: add another drink / remove a drink / view order / check out
6. On checkout, print the formatted receipt
"""

from menu_item import MenuItem
from order import Order

DRINKS = [
    ("Americano", 3.50),
    ("Cappuccino", 4.25),
    ("Espresso", 3.00),
    ("Latte", 4.75),
]

SIZES = [
    ("Small", 0.00),
    ("Medium", 0.75),
    ("Large", 1.25),
]


def show_drink_menu():
    # TODO: print the drink list with numbers and prices
    


def show_size_menu():
    # TODO: print the size list with numbers and upcharges
    


def choose_drink():
    """Prompt for a drink and size, return a new MenuItem."""
    # TODO: show drink menu, get choice (1-4)
    # TODO: show size menu, get choice (1-3)
    # TODO: compute price = base + upcharge
    # TODO: return MenuItem(name, size, price)
    


def main():
    # TODO: print welcome banner
    # TODO: ask for customer name and create an Order
    # TODO: add the first drink
    # TODO: loop showing the action menu (add / remove / view / check out)
    #       until the user checks out
    # TODO: on checkout, print the order (uses Order.__str__)
    print("************************************")
    print("Welcome to the Rodgers Coffee Shop!")
    print("************************************")
    customer_name = input("Enter customer name: ")
    current_order = Order(customer_name)
    print(f"Order created for {customer_name}.")

    while True:
        print("\n-- Main Menu ---")
        print("1. Add a drink")
        print("2. Remove a drink")
        print("3. View Current Order")
        print("4. Check Out")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\n-- Drink Menu ---")
            for drink, sizes in menu_items():
                print(f"- {drink}: {sizes}") 

            drink_name = input("Enter Drink name: ")
            if drink_name in menu 
                size = input(f"Enter size {list(menu[drink_name];keys())}:")
                if size in menu[drink_name]:
                    price = menu[drink_name][size]
                    item = MenuItem(drink_name, size, price)
                    current_order.add_item(item)
                    print(f"Added {item} to order.")
                else:
                    print("Invalid size.")
            else:
                print("Invalid drink name.")
           
        elif choice == "2":
            if not current_order.items:
                print("Order is empty.")
                continue
            for i, item in enumerate(current_order.items):
                print(f"{i+1}. {item}")
            try:
                item_index = int(input("Enter number of items to remove: ")) - 1
                removed_item = current_order.remove_item(item_index)
                if removed_item:
                    print(f"Removed {removed_item}.")
                else:
                    print("Invalid item number.")
            except ValueError
                print("Invalid input.")

        elif choice == "3":
            if not current_order.items:
                print("Order is empty.")
            else:
                current_order.print_receipt()

        elif choice == "4":
            current_order.print_receipt()
            print("Thank you for your order!")
            break
        
        else: 
            print("Invalid choice.")

if __name__ == "__main__":
    main()
