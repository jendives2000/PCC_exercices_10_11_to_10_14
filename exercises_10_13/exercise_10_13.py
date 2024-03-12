# Exercises from the book Python Crash Course by Eric Matthes.
# These exercises are about Storing Data and loading it using the json package.
# -----------------------------------------------------------------------------
# 1a. Expand the function gree_user  by asking for two more pieces of information about the user,
# 1a.1. then store all the information you collect in a dictionary.
# 1a.2. Write this dictionary to a file using json.dumps(),
# 2a. and read it back in using json.loads().
# 2a.1. Print a summary showing exactly what your program remembers about the user.

# -----------------------------------------------------------------------------

from pathlib import Path
import json

# -----------------------------------------------------------------------------
user_dictionary = {}


def greet_user():
    """Greet the user by name."""
    path_user_dict = Path("user.json")

    if path_user_dict.exists() and path_user_dict.read_text() == False:
        user_dictionary = json.loads(path_user_dict.read_text())
        username = user_dictionary["username"]
        print(f"Welcome back, {username}!")
    # 1a. Expand the function gree_user  by asking for two more pieces of information about the user,
    else:
        user_dictionary = {}
        username = input("\nWhat is your name? ")
        # 1a.1. then store all the information you collect in a dictionary.
        user_dictionary["username"] = username
        user_age = input("What is your age? ")
        user_dictionary["age"] = user_age
        user_height = input("How tall are you (in meter)? ")
        user_dictionary["height"] = user_height

        # 1a.2. Write this dictionary to a file using json.dumps(),
        dumpee = json.dumps(user_dictionary)
        path_user_dict.write_text(dumpee)
        print(f"\nYour details were saved to:\n\t{path_user_dict}\n")

        # 2a. and read it back in using json.loads().
        read_content = path_user_dict.read_text()
        # 2a.1. Print a summary showing exactly what your program remembers about the user.
        print(f"Please review them:\n\t")
        for key, value in user_dictionary.items():
            print(f"{key.title()}: {value}\n")


greet_user()
