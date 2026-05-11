"""
dvd.py - Week 8 Starter

DVD extends LibraryItem with runtime_minutes (int) and rating (str).
"""

from library_item import LibraryItem


class DVD(LibraryItem):

    def __init__(self, title, author, year, runtime_minutes, rating, checked_out=False):
        # TODO
        pass

    def get_item_type(self):
        # TODO: return "DVD"
        pass

    def __str__(self):
        # TODO: extend with runtime and rating
        pass
