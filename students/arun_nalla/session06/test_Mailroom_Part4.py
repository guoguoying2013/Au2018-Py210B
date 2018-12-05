#!usr/bin/env python
""" Testing Mailroom functions using pytest"""

from Mailroom import get_report
from Mailroom import donors_dict
from Mailroom import donors_list
from Mailroom import add_donors
from Mailroom import email_message
from Mailroom import path_to_store
from Mailroom import add_donation
import pytest
import random
import os

demo_dict = {'Abc':[1, 2], 'Xyz':[10]}

def test_donors_list():
    actual = list(demo_dict)
    assert actual == donors_list(demo_dict)

def test_add_donors():
    name = 'Arun'
    assert add_donors(name, demo_dict) == demo_dict.setdefault(name,[])
    assert 'Arun' in demo_dict
    assert len(demo_dict['Arun']) == 0
    assert 'ArunN' not in demo_dict


def test_add_donations():
    name = 'Arun'
    donation = 1
    expected_dict = {'Abc':[1, 2], 'Xyz':[10], name:[donation]}
    assert add_donation(name, demo_dict, donation) == expected_dict
    assert 1 in demo_dict['Arun']
    assert len(demo_dict['Arun']) == 1
    assert len(demo_dict['Abc']) == 2
    assert 1 not in demo_dict['Xyz']
    assert 10 not in demo_dict['Abc']

def test_get_report():
    expected_sorting = [('Xyz', 10, 1, 10.0), ('Abc', 3, 2, 1.5), ('Arun', 1, 1, 1.0)]
    assert get_report(demo_dict) == expected_sorting


def test_path_to_store():
    name = random.choice(list(demo_dict))
    assert path_to_store(name) == os.path.join(os.getcwd(), 'Mailroom', 'email_{}.txt'.format(name))
    expected_message = "Dear {},\nThank you for generous donation of ${:.2f}. It will be put to a good cause.\nSincerely,\nThe Team".format(name,sum(demo_dict[name]))
    assert email_message(name,sum(demo_dict[name])) == expected_message
