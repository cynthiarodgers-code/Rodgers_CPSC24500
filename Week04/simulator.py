"""
simulator.py - Week 5

Menu-driven Pet Simulator. Demonstrates polymorphism: the same methods
(feed, play, sleep) work on every pet type.

Menu:
1. Adopt a pet (cat / dog / fish)
2. Feed a pet
3. Play with a pet
4. Put a pet to sleep
5. View all pets
6. Quit
"""

from cat import Cat
from dog import Dog
from fish import Fish


def adopt_pet(pets):
    # TODO: ask which type, get name, create the right object, append to pets
    pet_type = input("Choose pet type (cat/dog/fish): ").lower()
    name = input("What is your pet's name? ")

    if pet_type == "cat":
        new_pet = Cat(name)
    elif pet_type == "dog":
        new_pet = Dog(name)
    elif pet_type == "fish":
        new_pet = Fish(name)
    else:
        print("Invalid pet type!")
        return

    pets.append(new_pet)
    print(f'{name} has been adopted!')

def select_pet(pets):
    """Show the list of pets and let the user pick one. Return the chosen pet."""
    # TODO: print numbered list of pets
    # TODO: get user choice and return that pet
    if not pets:
        print("You don't have any pets yet!")
        return None
    
    for i, pet in enumerate(pets):
        print(f"{i + 1}. {self._name}")

    choice = int(input("Select a pet by number: ")) - 1 


def main():
    
    # TODO: loop showing the menu and dispatching to the right action
    #       remember: feed/play/sleep should work the same regardless of pet type
    pets = []
    while True:
        print("\n1. Adopt 2. Select & Interact 3. Quit")
        choice = input("Action: ")
    
        if choice == "1":
            adopt_pet(pets)
        elif choice == "2":
            current_pet = select_pet(pets)
            if current_pet:
                action = input("Feed, Play, or Sleep? ").lower()
                if action =="feed":
                    current_pet.feed()
                elif action == "play":
                    current_pet.play()
                elif action == "sleep":
                    current_pet.sleep()
                else:
                    print("Invalid selection!")
                    return
        elif choice =="3":
            break



if __name__ == "__main__":
    main()
