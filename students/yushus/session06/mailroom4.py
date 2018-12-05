#!/usr/bin/env/python3

"""
Yushu Song
Au2018-Py210B
Mailroom4 assignment
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

def get_a_thank_you_letter(name, amount):
    letter = f'Dear {name},\n\n\tThank you for your generous donation of ${amount}.\n\n\tYour kindness is really making the world different!\n\n\t\tSincerely,\n\t\tMailroom Bot'
    return letter

def update_donation(name, amount, donor_db):

    # Each donation has to be non-negative amount and less than MAX value of the system allowed
    if amount <= sys.maxsize and amount > 0:
        donor_db[name].append(amount)
        return True
    else:
        raise ValueError('Donation has to be more than 0')

# Add donor if not exist
def update_donor(name, donor_db):

    # Check if name is null or empty
    if not name or name.isspace() or name is None:
        raise ValueError('Donor name cannot be empty!')

    # Keep a list of existing donor names in lower cases
    donors = [d.lower() for d in donor_db.keys()]
    if name.lower() not in donors:
        donor_db[name]=[]

# Send a thank you note for the donor
# The donor name is case insensitive
# However, the donor_db will keep the same case when donor name was first entered to the system
def send_a_thank_you():
    while True:
        try:
            name = input("Who do you want to send this to, use a full name: ")
            if name.lower() == 'list':
                print("\n".join(donor_db.keys()))
            else:
                update_donor(name, donor_db)
        except ValueError:
            print("Donor name cannot be empty!")
        else:
            break

    while True:
        try:
            amount = float(input("How much do you want to donate? "))
            if update_donation(name, amount, donor_db):
                print(get_a_thank_you_letter(name, amount))
        except ValueError:
            print("Please enter a valid donation!")
        else:
            break

# Given a path and file name, join them to a valid file structure
# If the path does not exist, create before joining
def get_file_name(path, file_name):

    # replace whitespace , * < > / \ ? % : | " . with underscore _
    file_name = re.sub(r'[\s+|,|*|<|>|/|\\|?|%|:|\||"|.]', '_', file_name)
    if not os.path.exists(path):
        os.mkdir(path)
    return os.path.join(path, f'{file_name}.txt')

# Send thank you letters to all donors
# Capture FileNotFoundError
def send_letters_to_all():
    for name in donor_db:
        try:
            with open(get_file_name(os.getcwd(), name), "w") as file:
                # Take the last donation made by the donor
                file.write(get_a_thank_you_letter(name, donor_db[name][-1]))
        except FileNotFoundError as fnf_error:
            print(fnf_error)

def get_report(donor_db):
    
    # sort the donors based on the total amount of money they donated
    donors = sorted(donor_db, key=lambda name:sum(donor_db[name]), reverse=True)
    report = []
    for name in donors:
        report.append([name, 
                       sum(donor_db[name]), 
                       len(donor_db[name]), 
                       sum(donor_db[name]) / len(donor_db[name])])
    
    return report

def create_a_report():
    header = "Donor Name                | Total Given | Num Gifts | Average Gift"
    line = "------------------------------------------------------------------"  
    print(f'{header}\n{line}')

    for donor in get_report(donor_db):
        print("{:26} ${:12.2f} {:10d} ${:13.2f}".format(*donor))

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