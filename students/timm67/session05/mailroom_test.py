#!/usr/bin/env/python3

"""
Tim Meese
Au2018-Py210B
Mailroom Part 4 assignment
"""

import pytest
from mailroom_part4 import create_report_task
from mailroom_part4 import send_thankyou_multiple_donors_task
from mailroom_part4 import send_thankyou_single_donor_test
from mailroom_part4 import add_single_donor_test
from pathlib import Path

# Duplicate donor database

donors = {
     ('Jim', 'Tillson'): [5.00, 20.00],
     ('Barb', 'Langley'): [10.00, 20.00, 100.00],
     ('Jen', 'Garfield'): [10.00, 20.00, 5.00],
     ('Rex', 'Miller'): [20.00, 20.00, 5.00],
     ('Tony', 'Blake'): [20.00, 20.00, 10.00]
     }

thankyou_file_list = []


def test_report():
    outlines = create_report_task()
    assert(5 == len(outlines))


def test_thankyou_files():
    global thankyou_file_list
    thankyou_file_list = send_thankyou_multiple_donors_task()
    for test_file in thankyou_file_list:
        try:
            test_file_path = Path(test_file)
            assert(test_file_path.is_file())
        except FileNotFoundError:
            assert(False)


def test_single_thankyou():
    fname = 'Jim'
    lname = 'Tillson'
    key = (fname, lname)
    donations = donors[key]
    thankyou_lines = send_thankyou_single_donor_test(key)
    assert fname in thankyou_lines[0]
    assert str(donations[(len(donations)-1)]) in thankyou_lines[1]


def test_single_thankyou_addnew():
    fname = 'Ada'
    lname = 'Fruit'
    key = (fname, lname)
    donations = [50.00]
    add_single_donor_test(fname, lname, donations)
    thankyou_lines = send_thankyou_single_donor_test(key)
    assert fname in thankyou_lines[0]
    assert str(donations[(len(donations)-1)]) in thankyou_lines[1]
    pass
