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
            donor_info[item[0].lower()].append(float(item[1]))
    return donor_info


def user_menu(db):
    menu = {1: menu_send_thank_you, 2: menu_create_report, 
    3: menu_all_donor_letters, 4: exit_program}
    response = input("\n\nSelect an option:\n  1  Send a thank you to a "
    "single donor\n  2  Create a report\n  3  Send letters to all donors"
    "\n  4  Quit\n\n> ")
    try:
        menu.get(int(response))(db)
    except(KeyError, ValueError):
        print("Please select 1, 2, 3, or 4.")


def menu_send_thank_you(db):
    donor = get_donor_name()
    amt = get_donation_amount()
    print(send_thank_you(db, donor, amt))


# Send a thank you
def send_thank_you(db, donor_name, donation_amount):
    if donor_name == 'list':
        for i in db.keys():
            print(i.title())
    else:
        db[donor_name].append(donation_amount)
        return generate_letter(db, donor_name)


def get_donor_name():
    return input("What is the donor's full name?\n> ").lower()


def get_donation_amount():
    try:
        return float(input("Please enter the donation amount.\n> "))
    except ValueError:
        print("Please enter a numeric donation amount.")


def generate_letter(db, donor_name):
    donor_name = donor_name.lower()
    name = donor_name.title()
    if len(db.get(donor_name)) > 1:
        donation_count = len(db.get(donor_name))
        donation_total = sum(db.get(donor_name))
        middle = ("You have donated {count} times for a total of "
        "${total:.2f}! ").format(count=donation_count, total=donation_total)
    else:
        middle = ("We greatly appreciate your generous contribution to "
        "our cause! ")

    letter = ("Dear {name},\nThank you for your recent donation in the "
    "amount of ${amount:.2f}.\n {middle} We will ensure that these funds "
    "are put to good use defending the universe.\nSincerely,\nThe Bravest "
    "Warriors")

    return letter.format(name=name, amount=db.get(donor_name)[-1], 
    middle=middle)


def get_path():
    valid_path = False
    while not valid_path:
        path = input("What directory do you want to write to?\n\n>  ")
        if not os.path.isdir(path):
            try:
                os.makedirs(path)
                valid_path = True
                return path
            except(FileExistsError, FileNotFoundError):
                print("Please enter a valid directory name.")
        else:
            valid_path = True
            return path


# Send thank you letters to all donors
def all_donor_letters(db, user_dir):
    dest = "{user_dir}/{date}_{name}.txt"
    date = datetime.datetime.today().strftime("%Y-%m-%d")
    for name in db.keys():
        path = dest.format(user_dir=user_dir, name=name, date=date)
        with open(path, "w") as f:
            f.write(generate_letter(db, name))


def menu_all_donor_letters(db):
    path = get_path()
    all_donor_letters(db, path)


# Create a report
def create_report(db):
    output = []
    colnames = ["Donor Name", "Total Given", "Num Gifts", "Avg Gift"]
    title = "\n\n{:<21}| {:>13} |{:>13} |{:>14}".format(colnames[0], 
    colnames[1], colnames[2], colnames[3])
    mystr = "{name:20} | ${total:>12.2f} | {count:>12} | ${avg:>12.2f}"
    output.append(title)
    output.append("---------------------|---------------|--------------"
    "|--------------")
    for name, donations in db.items():
        output.append(mystr.format(name=name.title(), total=sum(donations), 
        count=len(donations), avg=(sum(donations)/len(donations))))
    return output


def menu_create_report(db):
    for line in create_report(db):
        print(line)


def exit_program(db):
    sys.exit()


def main():
    donor_info = data_import('mailroom/donors.csv')
    while True:
        user_menu(donor_info)


if __name__ == "__main__":
    main()