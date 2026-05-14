"""
magazine.py - Week 8

Magazine extends LibraryItem with issue_number (int) and month (str).
"""

from library_item import LibraryItem


class Magazine(LibraryItem):

    def __init__(self, title, author, year, issue_number, month, checked_out=False):
        # TODO
        super().__init__(title, author, year, checked_out)
        self._issue_number = issue_number
        self._month = month

     @property
    def issue_number(self):
        return self._issue_number

    @property
    def month(self):
        return self._month

    def get_item_type(self):
        # TODO: return "Magazine"
        return "Magazine"

    def __str__(self):
        # TODO: extend with issue number and month
        base_str = super().__str__()
        return f"{base_str} [Issue #{self._issue_number}, {self._month}]"        
