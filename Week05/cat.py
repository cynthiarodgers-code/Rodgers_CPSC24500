"""
cat.py - Week 5

Cat extends Pet.
- Override feed() and play() with cat-specific behavior
- Add a unique purr() method
"""

from pet import Pet


class Cat(Pet):

    def __init__(self, name):
        # TODO: call super().__init__(name, "Cat")
        super().__init__(name, "Cat")

    def feed(self):
        # TODO: cat-specific feeding (different numbers than the base class)
        self._hunger -= 15
        self._energy += 10
        print("Eating! Hunger is now:", self._hunger)


    def play(self):
        # TODO: cat-specific play behavior
        self._happiness += 20
        self._energy -= 15
        print("Playing! Happiness is now:", self._happiness)

    def purr(self):
        # TODO: return a string like f"{self._name} purrs softly."
        return f"{self._name} purrs softly."
