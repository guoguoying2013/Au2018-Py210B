#!/usr/bin/env python

from mailroom import *

db = data_import('test_data.txt')

def test_data_import():
    mydata = data_import('test_data.txt')
    assert len(mydata.keys()) == 5
    assert mydata.get('one') == [1]
    assert mydata.get('three') == [1, 2, 3]
    assert mydata.get('decimal') == [1.8, 3.14]


def test_generate_letter_single_donation():
    result_one = ("Dear One,\nThank you for your recent donation in the "
    "amount of $1.00.\n We greatly appreciate your generous contribution to "
    "our cause!  We will ensure that these funds "
    "are put to good use defending the universe.\nSincerely,\nThe Bravest "
    "Warriors")
    assert generate_letter(db, 'one') == result_one

def test_generate_letter_multi_donation():
    result_three = ("Dear Three,\nThank you for your recent donation in the "
    "amount of $3.00.\n "
    "You have donated 3 times for a total of $6.00! "
    " We will ensure that these funds "
    "are put to good use defending the universe.\nSincerely,\nThe Bravest "
    "Warriors")
    assert generate_letter(db, 'three') == result_three

def test_send_ty_new_donor():
    result_five = ("Dear Five,\nThank you for your recent donation in the "
    "amount of $5.00.\n We greatly appreciate your generous contribution to "
    "our cause!  We will ensure that these funds "
    "are put to good use defending the universe.\nSincerely,\nThe Bravest "
    "Warriors")
    assert send_thank_you(db, 'five', 5) == result_five
    del db['five']

def test_send_ty_existing_donor():
    result_four = ("Dear Four,\nThank you for your recent donation in the "
    "amount of $4.00.\n "
    "You have donated 5 times for a total of $14.00! "
    " We will ensure that these funds "
    "are put to good use defending the universe.\nSincerely,\nThe Bravest "
    "Warriors")
    assert send_thank_you(db, 'four', 4) == result_four

def test_send_letters():
    today = datetime.datetime.today().strftime("%Y-%m-%d")
    assert os.path.isdir('thisisatest') == False
    os.makedirs('thisisatest')
    all_donor_letters(db, 'thisisatest')
    assert len(os.listdir('thisisatest')) == 5
    assert os.path.isfile('thisisatest/' + today + '_one.txt') == True
    os.remove('thisisatest/' + today + '_one.txt')
    assert os.path.isfile('thisisatest/' + today + '_two.txt') == True
    os.remove('thisisatest/' + today + '_two.txt')
    assert os.path.isfile('thisisatest/' + today + '_three.txt') == True
    os.remove('thisisatest/' + today + '_three.txt')
    assert os.path.isfile('thisisatest/' + today + '_four.txt') == True
    os.remove('thisisatest/' + today + '_four.txt')
    assert os.path.isfile('thisisatest/' + today + '_decimal.txt') == True
    os.remove('thisisatest/' + today + '_decimal.txt')
    os.rmdir('thisisatest')

def test_create_report():
    out = create_report(db)
    assert len(out) == 7
    assert out[0] == ('\n\nDonor Name           |   Total Given |    Num Gifts'
    ' |      Avg Gift')
    assert out[2] == ('One                  | $        1.00 |            1 |'
    ' $        1.00')
    assert out[4] == ('Three                | $        6.00 |            3 |'
    ' $        2.00')
    assert out[6] == ('Decimal              | $        4.94 |            2 |'
    ' $        2.47')