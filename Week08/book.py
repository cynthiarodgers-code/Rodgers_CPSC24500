"""
book.py - Week 8 

Book extends LibraryItem with isbn (str) and page_count (int).
"""

from library_item import LibraryItem


class Book(LibraryItem):

    def __init__(self, title, author, year, isbn, page_count, checked_out=False):
        # TODO: super().__init__(...)
        # TODO: store isbn and page_count
        pass

    def get_item_type(self):
        # TODO: return "Book"
        pass

    def __str__(self):
        # TODO: extend the base __str__ with ISBN and page count
        pass
