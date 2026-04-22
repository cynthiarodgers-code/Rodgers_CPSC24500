"""
pet.py - Week 5

The Pet base class. Subclasses (Cat, Dog, Fish) will inherit from this.

Constructor: name, species
Attributes: hunger (start 50), happiness (start 50), energy (start 50)

Methods:
- feed(): modifies hunger (and maybe other stats)
- play(): modifies happiness/energy
- sleep(): modifies energy
- status(): returns a formatted string showing all attributes
- __str__: returns name and species
"""


class Pet:

    def __init__(self, name, species):
        # TODO: store name and species
        # TODO: set hunger, happiness, energy each to 50
        self._name = name
        self._species = species
        self._hunger = 50
        self._happiness = 50

    def feed(self):
        # TODO: lower hunger (don't go below 0)
        self._hunger = max(0, self._hunger - 20)

    def play(self):
        # TODO: raise happiness, lower energy
        self._happiness += 10
        self._energy -= 10
        print("Playing! Happiness is now:", self._happiness)

    def sleep(self):
        # TODO: raise energy
        self._energy += 20
        print("Sleeping! Energy is now:", self._energy

    def status(self):
        # TODO: return a formatted string showing all three stats
        return f"{self._name} ({seld._species}): hunger={self._hunger}, happy={self._happiness}"

    def __str__(self):
        # TODO: return f"{self._name} the {self._species}"
        return f"{self._name} the {self._species}"
