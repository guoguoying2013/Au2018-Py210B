#!/usr/bin/env python

""" Mailroom_oo Main """

from mailroom_oo.donor_models import *


def newdonor():
    """ Adds new donor to the donorDB """

    while True:
        name = input("Please enter full name or list> ")
        if name == "":
            print("Please enter valid name.\n")
        elif name == "list":
            print(donor_database.donor_namelist())
        else:
            donationamount = input("Enter donation amount> ")
            donor_database.new_donor(name, donationamount)
            break


def exit_program():
    """Prints good bye and returns exit to end the loop"""

    print("Thank you. Bye")
    return "exit"


def main():
    """ Mailroom_oo main program loop with menu """

    donor_database = DonorCollection()

    menudict = {
        '1': newdonor,
        '2': printreport,
        '3': sendletters,
        '6': exit_program}

    mainmenu = "\n".join(("Welcome to the mailroom!",
                          "Please choose from below options:",
                          "1 - Add new donor to database",
                          "2 - Add donation to existing donor",
                          "3 - Send a Thank You letter",
                          "4 - Create a Report",
                          "5 - Send letters to all donors",
                          "6 - Quit",
                          ">>> "))

    while True:
        choice = input(mainmenu)

        try:
            if menudict.get(choice)() == "exit":
                break
        except TypeError:
            print("\nPlease enter a valid menu choice.\n")


if __name__ == "__main__":
    main()
