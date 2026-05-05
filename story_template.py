"""
story_template.py - Week 7 

A StoryTemplate holds a sentence pattern and can generate sentences from a WordCollection.

Pattern format: a list of strings.
- Literal words are plain strings: "The"
- Placeholders use braces: "{n}", "{v}", "{adj}", "{adv}", "{prep}"

Example:
    ["The", "{adj}", "{n}", "{v}", "{adv}"]

generate(words) walks through the pattern, replaces each placeholder with a random
word of that part of speech from the WordCollection, and returns the sentence
(capitalized, ending with a period).
"""

import random


class StoryTemplate:

    def __init__(self, name, pattern):
        # TODO: store name and pattern
        self._name = name
        self._pattern = pattern

    @property
    def name(self):
        return self._name

    @property
    def pattern(self):
        return self._pattern

    def generate(self, words):
            story_parts = []

        # TODO: walk through self._pattern
        for token in self._pattern:
        #   - if token starts with "{" and ends with "}", extract the POS
        #     and pick a random Word of that POS from `words`
        #   - otherwise keep the token as-is
            if token.startswith("{") and token.endswith("}"):
                pos = token[1:-1]
                if pos in words:
                     story_parts.append(random.choice(words[pos]))
                else:
                     story_parts.append(token)
            else:
                story_parts.append(token)
        # TODO: join with spaces, capitalize, add a period at the end
        story = " ".join(story_parts.capitalize() + ".")
        return story

# TODO: define at least 3 templates here
TEMPLATES = [
    StoryTemplate("Adventure", ["The", "{adj}", "{n}", "{v}", "{adv}", "{prep}", "the", "{adj}", "{n}"]),
    StoryTemplate("Mystery", ["A", "{adj}", "{n}", "was", "{v}", "in", "the", "{n}"]),
    StoryTemplate("Simple", ["The", "{n}", "{v}", "{adv}"])
]
