#!/usr/bin/env python3

import pytest
from donor_models import Donor
from donor_models import DonorCollection
from cli_main import MailroomCli


def test_donor_class():
    d = Donor('Ryan Seacrest', 1000.0)
    assert d.donor_name == 'Ryan Seacrest'
    assert d.donations[0] == 1000.0
    assert d.total_donations == 1000.0
    d.add_donation(500.0)
    assert d.last_donation == 500.0
    assert d.num_donations == 2
    assert d.avg_donation == ((1000.0 + 500.0) / 2.0)


def test_DonorCollection_class():
    dc = DonorCollection()
    dc.add_new_donor('Bill Gates')
    with pytest.raises(ValueError):
        dc.add_new_donor('Bill Gates')
    dc.add_donation('Bill Gates', 1000.0)
    d = dc.get_donor('Bill Gates')
    assert d.num_donations == 1
    assert d.total_donations == 1000.0
    assert d.donor_name == 'Bill Gates'
    dc.add_new_donor('Paul Allen')
    d2 = dc.get_donor('Paul Allen')
    d2.add_donation(2000.0)
    assert d2.num_donations == 1
    assert d2.total_donations == 2000.0
    assert d2.donor_name == 'Paul Allen'


def test_Climain():
    cli = MailroomCli()
    cli._dc.add_new_donor('Bill Gates')
    cli._dc.add_donation('Bill Gates', 2000.0)
    d3 = cli._dc.get_donor('Bill Gates')
    assert d3.num_donations == 1
    assert d3.total_donations == 2000.0
    assert d3.donor_name == 'Bill Gates'
    report_text = cli._dc.generate_report_all()
    assert report_text.count('Bill Gates') == 1
    assert report_text.count('2000.00') == 2
    filenames = cli._dc.generate_thankyou_all_to_file()
    assert filenames[1] == './Bill_Gates.txt'
    cli._dc.add_new_donor('Paul Allen')
    cli._dc.add_donation('Paul Allen', 3000.00)
    cli._dc.add_donation('Paul Allen', 3000.00)
    d4 = cli._dc.get_donor('Paul Allen')
    assert d4.num_donations == 2
    assert d4.total_donations == (3000.00 + 3000.00)
    assert d4.avg_donation == 3000.00
    assert d4.donor_name == 'Paul Allen'
    report_text = cli._dc.generate_report_all()
    assert report_text.count('Paul Allen') == 1
    assert report_text.count('3000.00') == 1
    assert report_text.count('6000.00') == 1
    filenames = cli._dc.generate_thankyou_all_to_file()
    assert filenames[2] == './Paul_Allen.txt'
