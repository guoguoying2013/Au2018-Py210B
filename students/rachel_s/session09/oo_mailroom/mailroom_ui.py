#!/usr/bin/env python3

"""session09, assignment oo mailroom, Rachel Schirra"""

import sys
import os
from donor_models import *

def user_menu(db):
    menu = {1: send_thank_you, 2: create_report, 
    3: all_donor_letters, 4: exit_program}
    response = input('\n\nSelect an option:\n  1  Send a thank you to a '
    'single donor\n  2  Create a report\n  3  Send letters to all donors'
    '\n  4  Quit\n\n> ')
    try:
        menu.get(int(response))(db)
    except(KeyError, ValueError):
        print('Please select 1, 2, 3, or 4.')


def send_thank_you(db):
    name = get_donor_name()
    if name in db.all_donors:
        d = db.get_donor(name)
        d.add_donation(get_donation_amount())
    else:
        db.add_new_donor(name, get_donation_amount())
        d = db.get_donor(name)
    print(d.generate_letter())


def create_report(db):
    print(db.generate_report())


def all_donor_letters(db):
    path = get_path()
    db.generate_all_letters(path)


def exit_program(db):
    sys.exit()


def get_donor_name():
    return input('What is the donor\'s full name?\n> ').lower().strip()


def get_donation_amount():
    return input('Please enter the donation amount.\n> ')


def get_path():
    valid_path = False
    while not valid_path:
        path = input('What directory do you want to write to?\n\n>  ')
        if not os.path.isdir(path):
            try:
                os.makedirs(path)
                valid_path = True
                return path
            except(FileExistsError, FileNotFoundError):
                print('Please enter a valid directory name.')
        else:
            valid_path = True
            return path


def main():
    dc = DonorCollection()
    dc.data_import('donors.csv')
    while True:
        user_menu(dc)


if __name__ == '__main__':
    main()