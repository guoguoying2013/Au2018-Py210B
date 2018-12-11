#!/usr/bin/env python

"""Pytest unit tests for the mailroom_oo module."""

from mailroom_oo.donor_models import *


def test_donor_init():
    d1 = Donor("Shawn DeGraw")
    d2 = Donor("Brandon Nguyen", 50.00)

    assert d1.name == "Shawn DeGraw"
    assert d1.donations == []

    assert d2.name == "Brandon Nguyen"
    assert d2.donations == [50.00]


def test_donor_manipulation():
    d1 = Donor("Shawn DeGraw")

    d1.add_donation(50.00)
    d1.add_donation(20.00)
    d1.add_donation(30.00)

    assert d1.donations == [50.00, 20.00, 30.00]
    assert d1.number_donations == 3
