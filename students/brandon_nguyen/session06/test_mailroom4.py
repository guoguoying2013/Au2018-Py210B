#!/usr/bin/env python3
# Week6 Excercise mailroom part 4b- the test file
# Student: Brandon Nguyen - Au2018
import sys
import time
import unittest
import os
from decimal import Decimal
from datetime import datetime, date
from mailroom4 import sort_sum4_report
from mailroom4 import update_donation
from mailroom4 import create_letters_text
from mailroom4 import create_files


input_db = {'FirstNameA LastNameA': [1, 1, 1, 11],
            'FirstNameB LastNameB': [2, 2, 2, 22],
            'FirstNameC LastNameC': [3, 3, 3, 33],
            }

TEST_LETTER = "\n".join(("", "Dear {Name},", "", "Thank you for your "
                         "kind donation of {LastAmnt:.2f}.",
                         "It will be put to very good use.", "",
                         "Sincerely, ", "", "-The Team\n"))


# Test 1: the sum list and sort for report in mailroom
def test_sort_sum4_report():
    expect_sum_db = [('FirstNameC LastNameC', [42], [4], [10.5]),
                     ('FirstNameB LastNameB', [28], [4], [7.0]),
                     ('FirstNameA LastNameA', [14], [4], [3.5]),
                     ]
    assert sort_sum4_report(input_db) == expect_sum_db


# Test 2: update_donation
def test_update_donation():
    empty_dict = {}
    input_list = ['First Last', 50]
    expected_test1 = {'First Last': [50]}
    # test empty dict
    assert update_donation(input_list, empty_dict) == expected_test1
    # test existing dict TODO


# Test 3: Verify the text in letters
def test_create_letters_text():
    dict_test3 = {'Brandon Nguyen': [100, 200, 300]}
    file_name = "Brandon_Nguyen_"+str(date.today()).replace(" ", "_")+".txt"
    expected_list = [(TEST_LETTER.format(Name='Brandon Nguyen', LastAmnt=300),
                      file_name)]
    assert create_letters_text(dict_test3) == expected_list


# Test 4: Verify file created
def test_create_files():
    file_name = "Brandon_Nguyen_"+str(date.today()).replace(" ", "_")+".txt"
    test4_list = [(TEST_LETTER.format(Name='Brandon Nguyen', LastAmnt=300),
                  file_name)]
    create_files(test4_list)
    assert os.path.isfile(file_name) == 1

