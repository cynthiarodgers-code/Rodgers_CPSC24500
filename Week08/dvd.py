"""
dvd.py - Week 8 Starter

DVD extends LibraryItem with runtime_minutes (int) and rating (str).
"""

from library_item import LibraryItem


class DVD(LibraryItem):

    def __init__(self, title, author, year, runtime_minutes, rating, checked_out=False):
        # TODO
        super().__init__(title, author, year, checked_out)
        self._runtime_minutes = runtime_minutes
        self._rating = rating
    
    @property
    def runtime_minutes(self):
        return self._runtime_minutes

    @property
    def rating(self):
        return self._rating

    def get_item_type(self):
        # TODO: return "DVD"
        return "DVD"       

    def __str__(self):
        # TODO: extend with runtime and rating
        base_str = super().__str__()
        return f"{base_str} [{self._runtime_minutes} mins, Rated {self._rating}]"        
