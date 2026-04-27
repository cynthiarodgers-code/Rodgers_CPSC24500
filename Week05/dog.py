"""
dog.py - Week 5 Starter

Dog extends Pet.
- Constructor takes an additional `breed` parameter
- Override feed() and play()
- Add a unique fetch() method
"""

from pet import Pet


class Dog(Pet):

    def __init__(self, name, breed):
        # TODO: call super().__init__(name, "Dog")
        # TODO: store breed
        super().__init__(name, "Dog")
        self._breed = breed

    def feed(self):
        # TODO: dog-specific feeding
        self._hunger -= 20
        self._energy += 15

    def play(self):
        # TODO: dog-specific play
        self._happiness += 10
        self._energy -= 10

    def fetch(self):
        # TODO: return a fetch-themed string
        return f"{self._name} fetches the ball happily."
