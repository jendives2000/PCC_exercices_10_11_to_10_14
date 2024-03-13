# Exercises from the book Python Crash Course by Eric Matthes.
# These exercises are about Storing Data and loading it using the json package.

# this exercise 10-13 was extended with the exercise 10-14. So, you are actually looking at 10-14.

# -----------------------------------------------------------------------------
# Exercise 10-13:
# 1a. Expand the function gree_user  by asking for two more pieces of information about the user,
# 1a.1. then store all the information you collect in a dictionary.
# 1a.2. Write this dictionary to a file using json.dumps(),
# 2a. and read it back in using json.loads().
# 2a.1. Print a summary showing exactly what your program remembers about the user.

# Exercise 10-14:
# Give the option to create new user details
# by refactoring relevant parts of your code  into at least one function for it

# -----------------------------------------------------------------------------

from pathlib import Path
import json

# -----------------------------------------------------------------------------
user_dictionary = {}


def greet_user():
    """Greet the user by name."""
    path_user_dict = Path("exercises_10_13/user.json")

    # happens if anyone comes back after inputting details.
    # So does NOT happen if it is the very first time
    if path_user_dict.exists() and path_user_dict.read_text():
        user_dictionary = json.loads(path_user_dict.read_text())
        username = user_dictionary["username"]
        print_a = f"\nWelcome back, {username}!"
        # Give the option to create new user details
        print_a += f"\nIf you are not {username}, you may type:"
        print(print_a)
        new_user_input = input("\n\t'c' to create a new user\n\tor 'q' to quit:\n--> ")

        # loop to get inputs while ruling out any input but 'q and 'c'
        while new_user_input not in ("q", "c"):
            print("\n--- Please, no numbers. ---\n" + new_user_input + "\n")
        # choice to quit
        if new_user_input == "q":
            print("\nBye for now.")
            exit()
        # choice to create new user details
        elif new_user_input == "c":
            print("\nGreat. Let's begin!")

            # by refactoring relevant parts of your code  into at least one function for it
            def inputs_for_user_dictionary():
                """Gets the user details from inputs and store them into a dictionary"""
                user_dictionary = {}
                username = input("\nWhat is your name? ")
                user_dictionary["username"] = username
                user_age = input("What is your age? ")
                user_dictionary["age"] = user_age
                user_height = input("How tall are you (in meter)? ")
                user_dictionary["height"] = user_height
                return user_dictionary

            new_user_dict = inputs_for_user_dictionary()

            def write_into_jsonfile():
                """Writes the user dictionary into a json file"""
                dumpee = json.dumps(new_user_dict)
                path_user_dict.write_text(dumpee)
                return dumpee

            write_into_jsonfile()
            print(f"\nYour details were saved to:\n\t{path_user_dict}\n")

            def confirm_and_print_jsonfile_content():
                """Review the content written to the json file by printing it"""
                read_content = path_user_dict.read_text()
                print(f"\nReading file:\n\t{read_content.strip()}\n")
                print(f"Please review your details:\n\t")
                for key, value in new_user_dict.items():
                    print(f"\t{key.title()}: {value}")
                print("\n")

            confirm_and_print_jsonfile_content()


greet_user()
