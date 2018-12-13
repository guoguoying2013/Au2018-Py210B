#!/usr/bin/env python3

"""session09, assignment oo mailroom, Rachel Schirra"""

import pytest
from mailroom_ui import *

def test_donor_class():
    d = Donor('Plum', 1700)
    assert d.name == 'Plum'
    assert d.donations == [1700]

    d = Donor('Jelly Kid')
    assert d.name == 'Jelly Kid'
    assert d.donations == []

def test_add_donation():
    d = Donor('Jelly Kid')
    d.add_donation(1)
    assert d.donations == [1]
    d.add_donation(2)
    d.add_donation(3)
    assert d.donations == [1, 2, 3]
    with pytest.raises(ValueError):
        d.add_donation('pineapple')

def test_add_negative_donation():
    d = Donor('Neg')
    with pytest.raises(ValueError):
        d.add_donation(-14)

def test_donor_params():
    d = Donor('Jelly Kid')
    d.add_donation(1)
    d.add_donation(2)
    d.add_donation(3)
    assert d.total_donations == 6
    assert d.avg_donation == 2
    assert d.count_donations == 3
    assert d.latest_donation == 3

def test_add_donor():
    dc = DonorCollection()
    dc.add_new_donor('Plum')
    dc.get_donor('Plum').add_donation(1)
    dc.get_donor('Plum').add_donation(2)
    dc.get_donor('Plum').add_donation(3)
    assert dc.get_donor('Plum').name == 'Plum'
    assert dc.get_donor('Plum').avg_donation == 2
    assert dc.get_donor('Plum').count_donations == 3
    assert dc.get_donor('Plum').latest_donation == 3

def test_generate_letter_single_donation():
    d = Donor("One", 1)
    result_one = ("Dear One,\nThank you for your recent donation in the "
    "amount of $1.00.\nWe greatly appreciate your generous contribution to "
    "our cause! We will ensure that these funds "
    "are put to good use defending the universe.\nSincerely,\nThe Bravest "
    "Warriors")
    assert d.generate_letter() == result_one

def test_generate_letter_multi_donation():
    d = Donor("Three")
    d.add_donation(1)
    d.add_donation(2)
    d.add_donation(3)
    result_three = ("Dear Three,\nThank you for your recent donation in the "
    "amount of $3.00.\n"
    "You have donated 3 times for a total of $6.00! "
    "We will ensure that these funds "
    "are put to good use defending the universe.\nSincerely,\nThe Bravest "
    "Warriors")
    assert d.generate_letter() == result_three

def test_generate_report_row():
    d = Donor('Plum')
    d.add_donation(1)
    d.add_donation(2)
    d.add_donation(3)
    row_output = ('Plum                 | $        6.00 |            3 |'
    ' $        2.00')
    assert d.generate_report_row() == row_output

def test_generate_report():
    dc = DonorCollection()
    dc.add_new_donor('Plum', 1)
    output = dc.generate_report()
    assert output[2:7] == 'Donor'
    assert 'Plum' in output

def test_all_letters():
    dc = DonorCollection()
    dc.add_new_donor('One', 1)
    dc.add_new_donor('Two', 1)
    dc.get_donor('Two').add_donation(2)
    dc.add_new_donor('Three', 1)
    dc.get_donor('Three').add_donation(2)
    dc.get_donor('Three').add_donation(3)
    today = datetime.datetime.today().strftime("%Y-%m-%d")
    assert os.path.isdir('thisisatest') == False
    os.makedirs('thisisatest')
    dc.generate_all_letters('thisisatest')
    assert len(os.listdir('thisisatest')) == 3
    assert os.path.isfile('thisisatest/' + today + '_one.txt') == True
    os.remove('thisisatest/' + today + '_one.txt')
    assert os.path.isfile('thisisatest/' + today + '_two.txt') == True
    os.remove('thisisatest/' + today + '_two.txt')
    assert os.path.isfile('thisisatest/' + today + '_three.txt') == True
    os.remove('thisisatest/' + today + '_three.txt')
    os.rmdir('thisisatest')
