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

path = Path(
    "\PYTHON\My_PYTHON_2024\PYTHON_practice\PCC_exercices_10_11_to_10_14\exercise_10_11\json_files/favorite_numbers.json"
)
if path.exists():
    read_content = path.read_text()  # 1b.
    saved_fav_num = json.loads(read_content)
    print(
        f"\nFetching your favorite number...\n\tHere it is: {saved_fav_num}\n"
    )  # 1b.1.
