#!/usr/bin/env python3
import sys
import tempfile

"""
Class: Python 210 B, Au2018
Exercise: Session 06, Mailroom Part 04
Student: Jason Jakubiak
"""

user_options = {
    "Send": "Send a Thank You to a single donor",
    "Report": "Create a Report",
    "Letter": "Send a letter to all donors",
    "Quit": "Quit",
    }

donor_db = {
    "jeff": [183.00, 200.00],
    "alex": [53898.23, 2653.00, 105.07],
    "paul": [33941.98],
    "mark": [1.65, 55.00],
    "john": [2705.71],
    }

thanks_txt = (
    "\nDear {},"
    "\nThank you for the donation of ${:.2f}."
    "\nSincerely,"
    "\nThe Mailroom Foundation\n"
    )

col_nm = ("Donor Name |", 
    "Total Given |",
    "Num Gifts |",
    "Average Gift |",
    )

row_sep = ('-' * sum([len(i) for i in col_nm]))

saved_txt = "Letters were successfully saved to "

menu_txt = ("\n Would you like to:"
    "\n 1 - {Send}"
    "\n 2 - {Report}"
    "\n 3 - {Letter}"
    "\n 4 - {Quit}"
    "\n >>> ")


def input_name():
    name = input("Please enter the full name: ").lower()
    return name


def input_amt():
    while True:
        try:
            amt = int(input("Please enter the donation amount: "))
            return amt
        except ValueError:
            print("Warning: Please enter an integer!\n")


def donor_list(donor_db):
    donor_nm = [donor.capitalize() for donor, amt in donor_db.items()]
    return donor_nm


def add_donor(name, amt, donor_db):
    donor_db.setdefault(name,[]).append(amt)


def create_msg(name, amt):
    msg = (thanks_txt.format(name.capitalize(), amt))
    return msg


def send_thanks():
    name = input_name()
    if name == "list":
        print(', '.join(donor_list(donor_db)))
    else:
        amt = input_amt()
        add_donor(name, amt, donor_db)
        print(create_msg(name, amt))


def sort_key(sort):
    return sort[1]


def donor_sort(donor_seq):
    donor_sort = sorted(donor_seq, key=sort_key, reverse=True)
    return donor_sort


def donor_calc(donor_db):
    donor_sum = [
            (donor.capitalize(), sum(amt), len(amt), sum(amt)/len(amt)) 
            for donor, amt in donor_db.items()
            ]
    return donor_sort(donor_sum)


def donor_rpt():
    print("{:13}{:<11}{:<11}{:<11}".format(*col_nm) + "\n" + row_sep)
    for donor, amt, len, avg in donor_calc(donor_db):
        print("{:13} ${:>11.2f}{:>11} ${:>11.2f}".format(donor, amt, len, avg))


def input_path():
    path = input("Please enter the path: ")
    if not path == "":
        path = path + "\\"
    return path


def write_letter(path, donor_db):
    for donor, amt, len, avg in donor_calc(donor_db):
        with open("{}{}.txt".format(path, donor), "w") as thank_you:
            thank_you.write(create_msg(donor, amt))


def print_thanks(path):
    if path != "":
        print(saved_txt + "{}".format((path)).replace("\\",""))
    else:
        print(saved_txt + "the current directory.")


def thanks_all():
    while True:
        try:
            path = input_path()
            write_letter(path, donor_db)
            print_thanks(path)
            return
        except FileNotFoundError:
            print("Warning: Please enter a valid path!\n")


def exit_program():
    print("Bye!")
    sys.exit()

switch_dict = {
    1: send_thanks,
    2: donor_rpt,
    3: thanks_all,
    4: exit_program,
    }


def menu(menu_txt, user_options):
    main_menu = (menu_txt.format(**user_options))
    return main_menu


def input_main():
    response = int(input(menu(menu_txt, user_options)))
    return response


def main():
    while True:
        try:
            switch_dict.get(input_main())()
        except TypeError:
            print("Warning: Please enter an valid option!")
        except ValueError:
            print("Warning: Please enter an valid integer!")

if __name__ == "__main__":
    main()
