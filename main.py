"""
main.py - Week 7 

Flow:
1. Ask for a path to a word file, load via WordCollection.from_file()
2. Print a count per part of speech
3. Show available story templates and let the user pick one
4. Ask how many sentences to generate
5. Generate and print the sentences
6. Ask if the user wants another story (loop if yes)
"""

from word_collection import WordCollection
from story_template import TEMPLATES


def main():
    # TODO: ask for the path; load the WordCollection
    path = input("Enter the path to the word file: ")
    words = WordCollection.from_file(path)
    # TODO: print summary (count per part of speech)
    print(words)
    # TODO: loop:
    #   - show templates with numbers
    #   - get user choice
    #   - ask how many sentences
    #   - call template.generate(words) for each
    #   - ask "Generate another story?" and break if not yes
    while True:
        print("\nAvailable Templates:")
        for i, temp in enumerate(TEMPLATES):
            print(f"{i}. {temp}")
        
        choice = int(input("Select a template number: "))
        selected_template = TEMPLATES[choice]

        num_sentences = int(input("How many sentences would you like to generate? "))

        prin("\n--- My Story ---")

        for _ in range(num_sentences):
            print(selected_template.generate(words))
        
        again = input("\nGenerate another story? (yes/no): ").lower().strip()
        if again != "yes":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
