"""
fish.py - Week 5

Fish extends Pet.
- Override feed() and play()
- Also override sleep() (fish don't sleep the same way)
"""

from pet import Pet


class Fish(Pet):

    def __init__(self, name):
        # TODO: call super().__init__(name, "Fish")
        super().__init__(name, "Fish")

    def feed(self):
        # TODO: fish-specific feeding
        self._hunger += 5
        self._energy += 10

    def play(self):
        # TODO: fish-specific play
        self._happiness += 10
        self._energy -= 5

    def sleep(self):
        # TODO: fish-specific sleep behavior (different from base class)
        return f"{self._name} swims sleepily."
