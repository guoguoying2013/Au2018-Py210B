#!/usr/bin/env python3
# Week6 Excercise mailroom part 4a - Refactor functions to test.
# Student: Brandon Nguyen - Au2018
import sys
import unittest
import os
from decimal import Decimal
from datetime import datetime, date
from os import makedirs


# global define data structure
# dictionary {person:[donations]}
donor_db = {"Brandon Nguyen": [4500.33, 350.87, 300.05],
            "Shawn DeGraw": [5500.00, 345.05, 571.33],
            "Jacqueline Lee": [4300.00, 3200.00, 230.13],
            "Aidan Nguyen": [4300.00, 200.00, 238.23],
            }
promptText = "\n".join(("\nWelcome to the mailroom program!\n",
                        "Please choose an options:\n\n",
                        "1 - Send a Thank You to a single donor.",
                        "2 - Create a Report.",
                        "3 - Send letters to all donors.",
                        "q - Quit",
                        ">>> "))

subMenuPrompt = ("Please Chose an option:\n\nlist - "
                 "To display a list of current donors.\n"
                 "1    - To enter name of donor to update.\n"
                 "q    - To exit this menu.\n"
                 ">>> ")              
# building switch case menu with dictionary
# think about a main menu function that can be called any where.

# Create a CONSTANT for email format.
E_FORMAT = "\n".join(("", "Dear {Name},", "", "Thank you for your "
                      "kind donation of {LastAmnt:.2f}.",
                      "It will be put to very good use.", "",
                      "Sincerely, ", "", "-The Team\n"))


def show_menu(promptxt, select_dict):
    while True:
        try:
            menu_selected = input(promptxt)
            if select_dict[menu_selected]() == 'Exit Menu':
                break
        except KeyError as err:
            print()
            print("You entered: {} incorrect option!".format(err))


def create_rpt():
    """
    This function is to print the report of donor.  
    """
    # Currently need more work on the format as 0.0 problem not yet solved.
    print()
    # creating new list with sorted total in reverse already for easy printing.
    newList = sort_sum4_report(donor_db)
    header_string = ("Donor Name              |  Total Given | Num Gifts |"
                     " Average Gift")
    line = '-'*len(header_string)
    print(header_string)
    print(line)
    for donor, total, num, avg in newList:
        print(" {:<18}     $  {:>12.2f} {:>6} {:>6} {:>8.2f}".
              format(donor, total[0], num[0], "$", avg[0]))
    print("\n\n")


# Test1 DONE
def sort_sum4_report(dict_db):
    # creating a new list with computed value for easy printing.
    """
    This function returned a sorted list of by on order amount
    """
    dblist = []
    dbSum = []
    # quick way to convert back to list to reuse existing code.
    # list comprehension
    [dblist.append((i, j)) for i, j in dict_db.items()]
    [dbSum.append((name, [round(sum(donation), 2)], [len(donation)],
     [round(sum(donation)/len(donation), 2)]),) for name, donation in dblist]
    return sorted(dbSum, key=lambda donor: donor[1], reverse=True)


# Test 2: business logic of updating the donor db DONE
def update_donation(input_val, dict_db):
    """
    To use this function please pass in two argument:
    input_val is a list with two set of value, donor_name, donation_value.
    db_dict is a replication of donor_db
    """
    # existing people add to donation
    if input_val[0] in dict_db:
        new_donation = dict_db.get(input_val[0])
        new_donation.append(input_val[1])
        dict_db[input_val[0]] = new_donation
    else:
        dict_db.update({input_val[0]: [input_val[1]]})
    return dict_db  # to support testing only so far


# Need to learn how to do unit test for userinput  TODO
def get_donation_input():
    """
    This func returns a list of two values: person name and donation amount.
    """
    input_person = input("\nPlease enter donor full names: ")
    while True:
        try:
            input_donation = float(input("Please enter donation amount for " +
                                   input_person + ":>> "))
            break
        except ValueError:
            print("\nPlease Reenter amount in float.")
    return [input_person, input_donation]


# Test #3
def create_letters_text(db):
    txt_list = []
    # makedirs("testDir")  # NEED to revisit this on mac 
    for personName in db:
        # assuming that the last donation appended to last
        # letter = email_template(personName, donor_db[personName][-1])
        tmp_dict = {"Name": personName, "LastAmnt": db[personName][-1]}
        letter = E_FORMAT.format(**tmp_dict)
        textfile = (personName.replace(" ", "_") + "_" +
                    str(date.today()).replace(" ", "_")+".txt")
        txt_list.append((letter, textfile),)
    return txt_list


# Test #4:
def create_files(in_list):
    for i in range(len(in_list)):
        with open(in_list[i][1], 'w') as file_object:
            file_object.write(in_list[i][0])


def list_donors():
    """
    Basic Name of donor return in Order by First Name
    """
    lst = []
    print()
    [lst.append(person) for person in donor_db]  # list comprehension converted
    lst.sort()
    for name in lst:
        print(name)
    print()


def input_donation_call(x):
    update_donation(x, donor_db)
    print()
    print(E_FORMAT.format(Name=x[0], LastAmnt=x[1]))


# a better way to exit from Chris video
def exit_menu():
    print("\nExiting the menu.")
    return "Exit Menu"


#  THIS IS WHERE WE HAVE FUNCTION for menus

def update_donation_call():
    input_donation_call(x=get_donation_input())


def send_ty():
    show_menu(subMenuPrompt, sub_menu_dict)


def send_all_letters():
    x_list = create_letters_text(donor_db)
    create_files(x_list)

# lesson learned - the value as function need to be below the defined function
# otherwise error - NameError 'send_ty' is not defined.
sub_menu_dict = {
                "list": list_donors,
                "1": update_donation_call,  # update donation,
                "q": exit_menu
                }

main_menu_dict = {
                '1': send_ty,
                '2': create_rpt,
                '3': send_all_letters,
                'q': exit_menu
                }


if __name__ == '__main__':
    show_menu(promptText, main_menu_dict)
