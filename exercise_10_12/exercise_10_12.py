# Exercises from the book Python Crash Course by Eric Matthes.
# These exercises are about Storing Data and loading it using the json package.
# -----------------------------------------------------------------------------
# Combine the two programs you wrote in Exercise 10-11 into one file.
# 1a. If the number is already stored,
# 1a.1. report the favorite number to the user.
# 1b. If not,
# 1b.1. prompt for the user’s favorite number
# 1b.2 and store it in a file.
# Run the program twice to see that it works.

# -----------------------------------------------------------------------------

from pathlib import Path
import json

# -----------------------------------------------------------------------------

path = Path(
    "\PYTHON\My_PYTHON_2024\PYTHON_practice\PCC_exercices_10_11_to_10_14\exercise_10_11\json_files/favorite_numbers.json"
)
read_content = path.read_text()

while True:
    if not path.exists() or not read_content:  # 1b. if no favorite number was stored.
        print_1 = '\nPress "q" to quit at anytime.'
        print_1 += "\nYou haven't saved a favorite number yet."
        favorite_number = input(
            f"{print_1}\n\nEnter your favorite number: --> "
        )  # 1b.1.

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
            path.write_text(dumpee)  # 1b.2.
            print(f"\nWe saved your favorite number at:\n\t{path}\n\n")
            break

    else:  # 1a.
        read_content = path.read_text()
        saved_fav_num = json.loads(read_content)
        print_a = "\nYou already saved your favorite number."
        print_a += f"\n\tHere it is: {saved_fav_num}\n"  # 1a.1.
        print(print_a)
        break
