#!/usr/bin/env python

"""Mailroom part 4 exercise. Contains the refactored code for doing unit testing."""

from os import makedirs,path
from pathlib import Path

# donor_db definition and default values

donor_db = {"John Smith": [500.00, 150.00, 20.00],
            "Jane Doe": [340.00, 30.00, 200.00],
            "Jason Bourne": [240.00, 140.00],
            "John Wick": [1000.00],
            "GI Jane": [150.00, 60.00]}


# Thank you letter templates
THANK_YOU_LETTER = "\n".join(("", "Dear {name},", "", "Thank you for your "
                              "generous donation of ${amount:.2f} to our "
                              "cause.", "Your donations help keep Python "
                              "great!", "", "Sincerely", "", "The Python "
                              "Project", ""))

GENERAL_DONATION_LETTER = "\n".join(("", "Dear {name},", "", "Thank you for "
                                     "your generosity in supporting us with "
                                     "${totaldonation:.2f} in donations.",
                                     "We hope to have your continued support.",
                                     "", "With great thanks", "", "The Python "
                                     "Project"))


def sumdbkey(donorlist):
    """Used by function sortdb to generate sort key
    :param donorlist: iterate through donordb tuples
    """
    return sum(donorlist[1])


def sortdb():
    """Returns a new db sorted on the sum of donations"""
    return sorted(donor_db.items(), key=sumdbkey, reverse=True)


def printthankyou(donorname):
    """Prints the thank you letter to standard output in mailroom part 1 format
    :param donorname: the index to the donor in the database the letter should
                     be addressed too
    """
    print(THANK_YOU_LETTER.format(name=donorname, amount=donor_db[donorname][-1]))


def getdonationamount(donorname):
    """User input function to collect donation amount from user
    :param donorname: the name of the donor to add the donation too
    """
    while True:
        donationamount = input("Enter donation amount> ")
        if adddonation(donorname, donationamount):
            break


def adddonation(donorname, donationammount):
    """Adds the donationamount to the supplied donorname
    :param donorname: the index to the donor in the database that the donation
                     should be added too
    :param donationamount: dollar amount to be added for the supplied donor
    """
    try:
        donor_db[donorname].append(float(donationammount))
    except ValueError:
        print("Error: Please enter a numeric dollar amount.\n")
        return False
    else:
        return True


def addnewdonordonation(name):
    """Creates a new donor in the donor_DB
    :param name: name of the new donor
    """
    donor_db[name] = []


def printdonorlist():
    """Prints a list of all donors in the db"""
    for name in donor_db:
        print(name)


def handlenames():
    """Determines if name provided is existing donor or new donor.
    Calls function to add donation to DB and calls function to
    print thank you letter"""

    while True:
        name = input("Please enter full name or list> ")
        if name == "":
            print("Please enter valid name.\n")
        elif name == "list":
            printdonorlist()
            break
        elif name in donor_db:
            getdonationamount(name)
            printthankyou(name)
            break
        else:
            addnewdonordonation(name)
            getdonationamount(name)
            printthankyou(name)
            break


def printreport():
    """Prints the report content"""
    report = createreport()
    print(report[0])
    print(report[1])
    print(report[2])


def createreport():
    """Creates report content"""
    newdb = sortdb()
    reporttitle = "\n{:<26}|{:^13}|{:^11}|{:^14}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift")
    reportseperator = "{:-<67}".format("")
    reportbody = ""
    for name, donation in newdb:
        reportbody += "{:<27}${:>11.2f} {:>11d}  ${:>12.2f}".format(name, sum(donation), len(donation), sum(donation)/len(donation))
        reportbody += "\n"
    print(reportbody)
    return (reporttitle, reportseperator, reportbody)


def sendletters():
    """Write a letter to a file for each donor.
       Letters put in Windows subdirectory called letters."""

    basedirectory = path.dirname(path.abspath(__file__))
    letterdirectory = Path(path.join(basedirectory, "letters"))

    if letterdirectory.is_dir():
        for donorname in donor_db:
            filename = path.join(letterdirectory, (donorname.replace(' ', '_') + ".txt"))
            # create a new dictionary just for the format mailroom part 2
            formatdict = {"name": donorname, "totaldonation": sum(donor_db[donorname])}
            try:
                with open(filename, 'w') as outfile:
                    outfile.write(GENERAL_DONATION_LETTER.format(**formatdict))
            except PermissionError:
                print("Error: Cannot create letters.")
                break
        print("Letters printed.\n")
    else:
        print("Error: letters directory must exist.")


def exit_program():
    """Prints good bye and returns exit to end the loop"""

    print("Thank you. Bye")
    return "exit"


def main():
    """Mailroom main program loop with menu"""

    menudict = {
        '1': handlenames,
        '2': printreport,
        '3': sendletters,
        '4': exit_program}

    mainmenu = "\n".join(("Welcome to the mailroom!",
                          "Please choose from below options:",
                          "1 - Send a Thank You",
                          "2 - Create a Report",
                          "3 - Send letters to all donors",
                          "4 - Quit",
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
