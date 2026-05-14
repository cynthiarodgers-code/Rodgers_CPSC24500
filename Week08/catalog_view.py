"""
catalog_view.py - Week 8 Starter

The View handles ALL display and output formatting. It does not store data
and does not modify the catalog.

Keep this class focused on printing. Anything that creates or modifies items
belongs in main.py (the controller).
"""


class CatalogView:

    def display_items(self, items):
        # TODO: print each item on its own line (uses __str__)
        # If empty, print "No items to display."
        if not items:
            print("No items to display.")
            return
        for item in items:
            print(item)

    def display_message(self, message):
        # TODO
        print(message)

    def display_menu(self):
        # TODO: print the main menu
        print("\n--- Main Menu ---")
        print("1. View Items")
        print("2. Search Items")
        print("3. Exit")

    def display_search_results(self, items, query):
        # TODO: print a header showing the query, then the items
        print(f"\n--- Search Results for '{query}' ---")
        self.display_items(items)
