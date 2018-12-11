#!/usr/bin/env python

""" Mailroom_oo - refactor in oject oriented design """


class Donor:
    """ Donor object
    :param name: donor's name
    :param initial_donation: optional initial donation value
    """

    def __init__(self, name, initial_donation=None):
        self.__name = name
        self.__donations = []
        if initial_donation is not None:
            self.__donations.append(initial_donation)

    @property
    def name(self):
        return self.__name

    @property
    def donations(self):
        return self.__donations

    @property
    def number_donations(self):
        return len(self.__donations)

    def __str__(self):
        return "{}, {}".format(self.__name, self.__donations)

    def add_donation(self, donation):
        self.donations.append(donation)


class DonorCollection:
    """ Holds collection of donor objects """

    pass
