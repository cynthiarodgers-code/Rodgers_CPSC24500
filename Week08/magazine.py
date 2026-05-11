"""
magazine.py - Week 8

Magazine extends LibraryItem with issue_number (int) and month (str).
"""

from library_item import LibraryItem


class Magazine(LibraryItem):

    def __init__(self, title, author, year, issue_number, month, checked_out=False):
        # TODO
        pass

    def get_item_type(self):
        # TODO: return "Magazine"
        pass

    def __str__(self):
        # TODO: extend with issue number and month
        pass
