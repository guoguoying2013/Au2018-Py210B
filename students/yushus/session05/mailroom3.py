#!/usr/bin/env/python3

"""
Yushu Song
Au2018-Py210B
Mailroom3 assignment
"""

import os
import random
import re
import sys

donor_db = {"William Gates, III": [653772.32, 12.17],
            "Jeff Bezos": [877.33],
            "Paul Allen": [663.23, 43.87, 1.32],
            "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
            "Elon Musk": [250000, 15000]}

prompt = "\n".join(("Welcome to mailroom bot!",
          "Please choose from below options:",
          "1 - Send a Thank You",
          "2 - Create a Report",
          "3 - Send letters to all donors",
          "4 - quit",
          ">>> "))

def print_donor():
    print("\n".join(donor_db.keys()))

def format_letter():
    letter = "\n".join(("Dear {name},\n",
             "\tThank you for your generous donation of ${amount}.\n",
             "\tYour kindness is really making the world different!\n",
             "\t\tSincerely,",
             "\t\tMailroom Bot"))
    
    return letter

def print_email(name, amount):
    print(format_letter().format(name=name, amount=amount))

# Send a thank you note for the donor
# The donor name is case insensitive
# However, the donor_db will keep the same case when donor name was first entered to the system
def send_a_thank_you():

    # maintain a donor list which contains donor names only
    donors = [d.lower() for d in donor_db.keys()]

    while True:
        name = input("Who do you want to send this to, use a full name: ")
        if name.lower() == 'list':
            print_donor()
        elif name.lower() not in donors: # New donor
            donor_db[name]=[]
            break
        else: # Existing donor; find the correct donor name from DB
            for donor_name in donor_db:
                if donor_name.lower() == name.lower():
                    name = donor_name
            break

    while True:
        try:
            # Each donation has to be non-negative amount and less than MAX value of the system allowed
            amount = float(input("How much do you want to donate? "))
            if amount <= sys.maxsize and amount > 0:
                donor_db[name].append(amount)
                print_email(name, amount)
            else:
                raise ValueError()
        except ValueError:
            print("Please enter a valid donation!")
        else:
            break

# Send thank you letters to all donors
# Capture FileNotFoundError
def send_letters_to_all():
    for name in donor_db:
        try:
            # replace whitespace , * < > / \ ? % : | " . with underscore _
            file_name = re.sub(r'[\s+|,|*|<|>|/|\\|?|%|:|\||"|.]', '_', name)
            with open(os.path.join(os.getcwd(), f"{file_name}.txt"), "w") as file:
                # Take the last donation made by the donor
                file.write(format_letter().format(name=name, amount=donor_db[name][-1]))
        except FileNotFoundError as fnf_error:
            print(fnf_error)

def create_a_report():
    header = "Donor Name                | Total Given | Num Gifts | Average Gift"
    line = "------------------------------------------------------------------"  
    print(header)
    print(line)

    # sort the donors based on the total amount of money they donated
    donor_names_sorted = sorted(donor_db, key=lambda name:sum(donor_db[name]), reverse=True)

    for name in donor_names_sorted:
        print("{:26} ${:12.2f} {:10d} ${:13.2f}".format(name, 
                                                        sum(donor_db[name]), 
                                                        len(donor_db[name]), 
                                                        sum(donor_db[name]) / len(donor_db[name])))

def exit_program():
    print("Bye!")
    sys.exit()  # exit the interactive script

def main():
    while True:
        try:
            response = input(prompt)  # continuously collect user selection
            choice_dict[response.strip()]()
        except Exception as ex:
            print(f"You got an error {ex}. Please choose 1-4!")

choice_dict = {"1":send_a_thank_you,
               "2":create_a_report,
               "3":send_letters_to_all,
               "4":exit_program}

if __name__ == "__main__":
    # don't forget this block to guard against your code running automatically if this module is imported
    main()