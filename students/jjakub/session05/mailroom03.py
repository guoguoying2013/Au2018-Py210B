#!/usr/bin/env python3
import sys
import tempfile

"""
Class: Python 210 B, Au2018
Exercise: Session 05, Mailroom Part 03
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


def sort_key(sort):
    return sort[1]


def send_thanks():
    name = ''
    while not name or name.lower() == 'list':
        name = input("Please enter the full name: ").lower()
        if name == 'list':
            print(' '.join(donor_db))
    while True:
        try:
            amt = int(input("Please enter the donation amount: "))
            donor_db.setdefault(name,[]).append(amt)
            print(f'\nDear {name.capitalize()},\
                    \nThank you for the donation of ${amt:.2f}.\nSincerely,\
                    \nThe Mailroom Foundation')
            return
        except ValueError:
            print("\n Warning: Please enter an integer! \n")


def donor_calc(donor_db):
    donor_sum = [
            (donor.capitalize(), sum(amt), len(amt), sum(amt)/len(amt)) 
            for donor, amt in donor_db.items()
            ]
    return donor_sort(donor_sum)


def donor_sort(donor_seq):
    donor_sort = sorted(donor_seq, key=sort_key, reverse=True)
    return donor_sort


def donor_rpt():
    header = (
        "{:13}{:<11}{:<11}{:<11}"
        .format('Donor Name |', 'Total Given |', 'Num Gifts |', 'Average Gift |')
        )
    seperator = '-' * 47
    print(header + "\n" + seperator)
    for donor, amt, len, avg in donor_calc(donor_db):
        print("{:13} ${:>11.2f}{:>11} ${:>11.2f}".format(donor, amt, len, avg))


def thanks_all():
    while True:
        try:    
            path = input("Please enter the path: ")
            if path != '':
                path = path + "\\"
            for donor, amt, len, avg in donor_calc(donor_db):
                with open("{}{}.txt".format(path, donor), "w") as thank_you:
                    thank_you.write("\n Dear, {} \
                                    \n Thank you for the donation of ${} \
                                    \n Sincerely, \
                                    \n The Mailroom Foundation".format(donor, amt))

            if path != '':
                print("\n Letters were successfully saved to {}.\n".format(path))
            else:
                print("\n Letters were successfully saved to the current directory.\n")
            return

        except FileNotFoundError:
            print("\n Warning: Please enter a valid path!\n")


def exit_program():
    print("Bye!")
    sys.exit()


switch_dict = {
    1: send_thanks,
    2: donor_rpt,
    3: thanks_all,
    4: exit_program,
    }


def main():
    main_menu = ("\n Would you like to: \
        \n 1 - {Send}\
        \n 2 - {Report}\
        \n 3 - {Letter}\
        \n 4 - {Quit}\
        \n >>> ".format(**user_options)
        )
    while True:
        try:
            response = int(input(main_menu))
            switch_dict.get(response)()
        except TypeError:
            print("\n Warning: Please enter an valid integer!")
        except ValueError:
            print("\n Warning: Please enter a valid option!")

if __name__ == "__main__":
    main()
