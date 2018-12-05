#!/usr/bin/env python3

import csv
import os
import datetime
import sys
from collections import defaultdict

# Import donor data
def data_import(filename):
    donor_info = defaultdict(list)
    csv_list = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        csv_list = [line for line in csv_reader]
        for item in csv_list:
            donor_info[item[0].lower()].append(int(item[1]))
    return donor_info


donor_info = data_import('mailroom/donors.csv')


def user_menu():
    menu = {1: send_thank_you, 2: create_report, 3: all_donor_letters, 
    4: exit_program}
    response = input("\n\nSelect an option:\n  1  Send a thank you to a "
    "single donor\n  2  Create a report\n  3  Send letters to all donors"
    "\n  4  Quit\n\n> ")
    try:
        menu.get(int(response))()
    except(KeyError, ValueError):
        print("Please select 1, 2, 3, or 4.")


# Send a thank you
def send_thank_you():
    donor_name = input("What is the donor's full name?\n> ").lower()
    if donor_name == 'list':
        for i in donor_info.keys():
            print(i.title())
    else:
        try:
            donation = int(input("Please enter the donation amount.\n> "))
            donor_info[donor_name.lower()].append(donation)
            print(generate_letter(donor_name))
        except ValueError:
            print("Please enter a numeric donation amount.")


def generate_letter(donor):
    donor = donor.lower()
    name = donor.title()
    if len(donor_info.get(donor)) > 1:
        donation_count = len(donor_info.get(donor))
        donation_total = sum(donor_info.get(donor))
        middle = ("You have donated {count} times for a total of "
        "${total:.2f}! ").format(count=donation_count, total=donation_total)
    else:
        middle = ("We greatly appreciate your generous contribution to "
        "our cause! ")

    letter = ("Dear {name},\nThank you for your recent donation in the "
    "amount of ${amount:.2f}. {middle} We will ensure that these funds "
    "are put to good use defending the universe.\nSincerely,\nThe Bravest "
    "Warriors")

    return letter.format(name=name, amount=donor_info.get(donor)[-1], 
    middle=middle)


# Send thank you letters to all donors
def all_donor_letters():
    user_dir = input("What directory do you want to write to?\n\n>  ")
    dest = "{user_dir}/{date}_{name}.txt"
    date = datetime.datetime.today().strftime("%Y-%m-%d")
    if not os.path.isdir(user_dir):
        os.makedirs(user_dir)
    for name in donor_info.keys():
        path = dest.format(user_dir=user_dir, name=name, date=date)
        with open(path, "w") as f:
            f.write(generate_letter(name))


# Create a report
def create_report():
    colnames = ["Donor Name", "Total Given", "Num Gifts", "Avg Gift"]
    title = "{:<21}| {:>13} |{:>13} |{:>14}".format(colnames[0], colnames[1],
     colnames[2], colnames[3])
    mystr = "{name:20} | ${total:>12.2f} | {count:>12} | ${avg:>12.2f}"
    print(title)
    print("---------------------|---------------|--------------"
    "|--------------")
    for name, donations in donor_info.items():
        print(mystr.format(name=name.title(), total=sum(donations), count=len
        (donations), avg=(sum(donations)/len(donations))))

def exit_program():
    sys.exit()

def main():
    while True:
        user_menu()


if __name__ == "__main__":
    main()