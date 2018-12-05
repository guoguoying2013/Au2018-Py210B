#!/usr/bin/env python

"""
Class: Python 210 B, Au2018
Exercise: Session 06, Mailroom Part 04 Unit Test
Student: Jason Jakubiak
"""

from mailroom04 import *
import mailroom04
import os.path

test_name = "name"
test_amt = 9999
test_db_in = {}
path = test_name + ".txt"

test_db = {
    test_name: [test_amt]
    }

test_list_out = ["Name"]

test_txt = (
    "\nDear Name,"
    "\nThank you for the donation of $9999.00."
    "\nSincerely,"
    "\nThe Mailroom Foundation\n"
    )


test_sort_in = [
    ('A', 3),
    ('B', 1),  
    ('C', 2),
    ('D', 4),
    ]

test_sort_out = [
    ('D', 4),
    ('A', 3),
    ('C', 2),
    ('B', 1),
    ]

test_db_calc = [
    (test_name.capitalize(), test_amt, 1, test_amt)
    ]


def test_add_donor():
    mailroom04.add_donor(test_name, test_amt, test_db_in)
    assert test_db_in == test_db


def test_donor_list():
    assert donor_list(test_db) == test_list_out


def test_create_msg():
    assert mailroom04.create_msg(test_name,test_amt) == test_txt


def test_donor_sort():
    assert mailroom04.donor_sort(test_sort_in) == test_sort_out


def test_donor_calc():
     assert mailroom04.donor_calc(test_db) == test_db_calc


def test_write_letter():
    mailroom04.write_letter("", test_db)
    assert os.path.exists(path)


def test_contents():
    file = open(path, "r")
    letter = file.read()
    file.close()
    os.remove(path)
    assert letter == test_txt
