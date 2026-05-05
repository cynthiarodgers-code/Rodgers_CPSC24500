"""
word_collection.py - Week 7

Holds a list of Word objects and supports iteration, indexing, filtering, and sorting.

Operator overloading:
- __len__, __getitem__, __contains__, __iter__, __repr__

Methods:
- add(word): TypeError if not a Word
- filter_by_pos(pos): returns a NEW WordCollection
- sorted_words(reverse=False): returns a NEW WordCollection sorted via Word.__lt__
- from_file(filepath): @classmethod that reads "word pos" lines and returns a WordCollection
"""

from word import Word


class WordCollection:

    def __init__(self):
        # TODO: empty internal list
        self._words = []

    @classmethod
    def from_file(cls, filepath):
        # TODO: create a new WordCollection
        collection = cls()
        # TODO: open the file, read each line
        #   - strip; skip blank lines
        #   - split into text and pos; skip lines that don't parse
        #   - create a Word and add it (catch ValueError for invalid POS)
        with open(filepath, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                parts = line.split()
                if len(parts) != 2:
                    continue

                text, pos = parts

                try:
                    word = Word(text, pos)
                    collection.add(word)
                except ValueError:
                    continue
        # TODO: return the collection
        return collection

    def add(self, word):
        # TODO: raise TypeError if not a Word
        # TODO: append to internal list
        if not isinstance(word, Word):
            raise TypeError("Only Word objects can be added to WordCollection")
        
        self._words.append(word)

    def filter_by_pos(self, part_of_speech):
        # TODO: build a new WordCollection containing only matching words
        filtered = WordCollection()
        for word in self._words:
            if word.part_of_speech == part_of_speech:
                filtered.add(word)
        return filtered

    def sorted_words(self, reverse=False):
        # TODO: build a new WordCollection from sorted(self._words, reverse=reverse)
        # No `key` parameter -- relies on Word.__lt__
        sorted_coll = WordCollection()
        for word in sorted(self._words, reverse=reverse):
            sorted_coll.add(word)
        return sorted_coll

    def __len__(self):
        # TODO
        return len(self._words)

    def __getitem__(self, index):
        # TODO
        return self._words[index]

    def __contains__(self, item):
        # TODO
        return item in self._words

    def __iter__(self):
        # TODO: return iter(self._words)
        return iter(self._words)

    def __repr__(self):
        # TODO: return f"WordCollection({len(self)} words)"
        return f"WordCollection({len(self)} words)"
