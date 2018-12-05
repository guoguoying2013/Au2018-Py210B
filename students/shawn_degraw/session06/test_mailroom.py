#!/usr/bin/env python

"""Pytest unit tests for the mailroompart4.py module."""

import mailroompart4
from os import makedirs,path
from pathlib import Path


def test_sortDB():
    assert mailroompart4.sortdb() == [('John Wick', [1000.0]), ('John Smith', [500.0, 150.0, 20.0]), ('Jane Doe', [340.0, 30.0, 200.0]), ('Jason Bourne', [240.0, 140.0]), ('GI Jane', [150.0, 60.0])]


def test_report():
    report = mailroompart4.createreport()
    assert report[0] == ('\nDonor Name                | Total Given | Num Gifts | Average Gift ')
    assert report[1] == ('-------------------------------------------------------------------')
    assert report[2] == ('John Wick                  $    1000.00           1  $     1000.00\nJohn Smith'
                         '                 $     670.00           3  $      223.33\nJane Doe             '
                         '      $     570.00           3  $      190.00\nJason Bourne               $   '
                         '  380.00           2  $      190.00\nGI Jane                    $     210.00   '
                         '        2  $      105.00\n')


def test_posadddonation():
    assert mailroompart4.adddonation("John Wick", 20) == True


def test_negaddonation():
    assert mailroompart4.adddonation("John Wick", "test") == False


def test_successfuladddonation():
    mailroompart4.adddonation("John Smith", 100)
    assert mailroompart4.donor_db["John Smith"] == [500.0, 150.0, 20.0, 100.0]


def test_newdonoradd():
    mailroompart4.addnewdonordonation("Test User")
    assert "Test User" in mailroompart4.donor_db.keys()


def test_lettercreated():
    mailroompart4.sendletters()
    # generate path to directory holding letters
    basedirectory = path.dirname(path.abspath(__file__))
    letterdirectory = path.join(basedirectory, "letters")

    testfile_janedoe = Path(path.join(letterdirectory, "Jane_Doe.txt"))
    testfile_johnwick = Path(path.join(letterdirectory, "John_Wick.txt"))
    testfile_gijane = Path(path.join(letterdirectory, "GI_Jane.txt"))
    testfile_johnsmith = Path(path.join(letterdirectory, "John_Smith.txt"))
    testfile_jasonbourne = Path(path.join(letterdirectory, "Jason_Bourne.txt"))

    assert path.isfile(testfile_janedoe) == True
    assert path.isfile(testfile_johnwick) == True
    assert path.isfile(testfile_gijane) == True
    assert path.isfile(testfile_johnsmith) == True
    assert path.isfile(testfile_jasonbourne) == True


def test_lettercontent():
    mailroompart4.sendletters()
    # generate path to directory holding letters
    basedirectory = path.dirname(path.abspath(__file__))
    letterdirectory = path.join(basedirectory, "letters")
    testfile_janedoe = Path(path.join(letterdirectory, "Jane_Doe.txt"))

    try:
        with open(testfile_janedoe, 'r') as infile:
            testfile = infile.read()
    except FileNotFoundError:
        testfile = "file read error"
    
    assert testfile == ("\nDear Jane Doe,\n\nThank you for your generosity in supporting us with "
                        "$570.00 in donations.\nWe hope to have your continued support.\n\nWith great thanks\n\nThe Python Project")
