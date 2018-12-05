#!/usr/bin/env python
'''pytest test harnesses for Mailroom Part 4 for Session 6, Python 210
Written by David K. Arasim - 11/13/18
Covers all items as required by, and identified in the assignment'''

# Imported modules to be tested
import mailroom4

# Imported modules
import os
from collections import defaultdict

# Global variables
form_text = 'Dear {form_name},\n'
form_text += 'Thank you for your generous donation of ${form_amt:.2f}\n'
form_text += 'Please consider this e-mail as record of your donation for tax deduction purposes.\n'
form_text += 'Sincerely, Your Local Charity'

form_text_out = 'Dear Test Name,\n'
form_text_out += 'Thank you for your generous donation of $100.99\n'
form_text_out += 'Please consider this e-mail as record of your donation for tax deduction purposes.\n'
form_text_out += 'Sincerely, Your Local Charity'

form_name = 'Test Name'
form_amt = 100.99

donor_dict = defaultdict(list)

donor_dict_add = defaultdict(list)
donor_dict_add[form_name].append(float(form_amt))

donor_dict_update = defaultdict(list)
donor_dict_update[form_name].append(float(form_amt))
donor_dict_update[form_name].append(float(form_amt))

donor_list = 'List of Donors            \n'
donor_list += '--------------------------\n'
donor_list += 'Test Name                 \n\n'

donor_rpt = 'Donor Name                |  Total Given|  Num Gifts| Average Gift\n'
donor_rpt += '------------------------------------------------------------------\n'
donor_rpt += 'Test Name                  $      100.99           1 $      100.99\n'


########################################################################################################
# Itemized test functions

def test_build_form_text():
    # Send Thank You:  Generating thank you text (unformatted)
    assert mailroom4.build_form_text() == form_text


def test_build_form_text_out():
    # Send Thank You:  Generating thank you text (formatted)
    assert mailroom4.build_form_text_out(form_name, form_amt) == form_text_out


def test_find_donor_add():
    # Send Thank You:  Adding or updating donors (add)
    mailroom4.find_donor(donor_dict, form_name, form_amt)
    assert donor_dict == donor_dict_add


def test_find_donor_update():
    # Send Thank You:  Adding or updating donors (update)
    mailroom4.find_donor(donor_dict_add, form_name, form_amt)
    assert donor_dict_add == donor_dict_update


def test_show_donor_list():
    # Send Thank You:  Listing Donors
    assert mailroom4.show_donor_list(donor_dict_add) == donor_list


def test_create_report():
    # Create Report:  Reporting Donors
    assert mailroom4.create_report(donor_dict, True) == donor_rpt


def test_send_all_thanks():
    # Send Letters:  Verify file creation and content
    mailroom4.send_all_thanks(donor_dict)

    textfile_found = False

    try:
        with open('Test_Name.txt', 'r') as textfile:
            textfile_found = True

            textfile_content = textfile.read()

        textfile.close()
    except FileNotFoundError:
        textfile_content = ''

    assert textfile_found == True
    assert textfile_content == form_text_out