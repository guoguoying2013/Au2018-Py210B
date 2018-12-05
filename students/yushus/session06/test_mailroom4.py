#!/usr/bin/env/python3

"""
Yushu Song
Au2018-Py210B
Mailroom4 assignment
"""

import os
import pytest
import re
import sys
import shutil
from mailroom4 import get_report, get_file_name, update_donor, update_donation, get_file_name, get_a_thank_you_letter

def test_get_report_success():
    donor_db = {"Bill Gates": [100, 200],"Jack Ma": [500, 500]}
    assert get_report(donor_db) == [["Jack Ma", 1000, 2, 500],
                                    ["Bill Gates", 300, 2, 150]]

def test_update_donor_success():
    donor_db = {"Bill Gates": [100, 200],"Jack Ma": [500, 500]}
    update_donor("Yushu Song", donor_db)
    assert "Yushu Song" in donor_db.keys()

def test_update_donor_failure():
    with pytest.raises(ValueError, match=r'Donor name.*'):
        update_donor("", {})

def test_update_donation_success():
    donor_db = {"Bill Gates": [100, 200],"Jack Ma": [500, 500]}
    update_donation("Bill Gates", 300, donor_db)
    assert donor_db["Bill Gates"][-1] == 300

def test_update_donation_failure():
    donor_db = {"Bill Gates": [100, 200],"Jack Ma": [500, 500]}
    with pytest.raises(ValueError, match=r'.*\s+0'):
        update_donation("Bill Gates", 0, donor_db)

def test_get_file_name_replace_char_success():
    path = os.getcwd()
    file_name = "Yushu*Song"
    assert os.path.join(path, "Yushu_Song.txt") == get_file_name(path, file_name)

def test_get_file_name_new_dir_success():
    try:
        path = os.path.join(os.getcwd(), 'temp')
        file_name = "Yushu*Song"
        assert os.path.join(path, "Yushu_Song.txt") == get_file_name(path, file_name)
    except Exception as ex:
        print(ex)
    finally:
        # Clean up resource afterwards
        shutil.rmtree(path)

def test_get_a_thank_you_letter_success():
    name = "Yushu Song"
    amount = 1000
    assert name and str(amount) in get_a_thank_you_letter(name, amount)