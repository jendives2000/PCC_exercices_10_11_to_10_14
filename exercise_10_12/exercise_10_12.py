# Exercises from the book Python Crash Course by Eric Matthes.
# These exercises are about Storing Data and loading it using the json package.
# -----------------------------------------------------------------------------
# 1a. Write a program that prompts for the user’s favorite number.
# 1a.1. Use json.dumps() to store this number in a file.
# 1b. Write a separate program that reads in this value
# 1b.1. and prints the message “I know your favorite number! It’s _____.”

# -----------------------------------------------------------------------------

from pathlib import Path
import json

# -----------------------------------------------------------------------------

# 1a. Write a program that prompts for the user’s favorite number.
path = Path(
    "\PYTHON\My_PYTHON_2024\PYTHON_practice\PCC_exercices_10_11_to_10_14\exercise_10_11\json_files/favorite_numbers.json"
)
read_content = path.read_text()

while True:
    if (
        not path.exists() or not read_content
    ):  # if the json file doesn't exist OR is empty
        print_1 = '\nPress "q" to quit at anytime.'
        print_1 += "\nYou haven't saved a favorite number yet."
        favorite_number = input(f"{print_1}\n\nEnter your favorite number: --> ")

        while not favorite_number.isnumeric():
            if favorite_number == "q":
                print("\nThank you!\nExiting now.\n")
                exit()
            elif favorite_number != "q":
                print("\n--- Please no letters. ---")
                break
        if favorite_number.isnumeric():
            print(f"\nThank you!\nThis is your favorite number:\n\t{favorite_number}")
            dumpee = json.dumps(favorite_number)
            path.write_text(dumpee)
            print(f"\nWe saved your favorite number at:\n\t{path}\n\n")
            break

    else:
        read_content = path.read_text()
        saved_fav_num = json.loads(read_content)
        print_a = "\nYou already saved your favorite number."
        print_a += f"\n\tHere it is: {saved_fav_num}\n"
        print(print_a)
        break

# 1a.1. Use json.dumps() to store this number in a file.

# 1b. Write a separate program that reads in this value
