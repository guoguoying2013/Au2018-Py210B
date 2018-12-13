#!/usr/bin/env python3

"""
Tim Meese
Au2018-Py210B
Mailroom Object Oriented assignment
"""


class Donor(object):
    """
    Donor class
    """
    def __init__(self, initial_name, initial_donation=None):
        self._name = initial_name
        self._donations = []
        self._last_donation = float(0.0)
        if initial_donation is not None:
            self.add_donation(initial_donation)

    def __str__(self):
        return "Donor: name={}, donatns={}".format(self._name, self._donations)

    @property
    def donor_name(self):
        return self._name

    @property
    def donations(self):
        return self._donations

    @property
    def last_donation(self):
        return self._last_donation

    @property
    def num_donations(self):
        return len(self._donations)

    @property
    def total_donations(self):
        return sum(self._donations)

    @property
    def avg_donation(self):
        return float(self.total_donations / self.num_donations)

    def add_donation(self, donation):
        if not isinstance(donation, float):
            donation = float(donation)
        self._donations.append(donation)
        self._last_donation = donation

    def generate_report_row(self):
        report_fmt_str = "{0:20}{1:10}{2:10.2f}{3:10.2f}"
        return report_fmt_str.format(self.donor_name, self.num_donations,
                                     self.total_donations, self.avg_donation)

    def generate_text(self):
        outlines = []
        fmtline0 = "\n\nDear {0},\n\n"
        fmtline1 = "Many thanks for your recent donation of {0:6.2f}.\n\n"
        fmtline2 = "Your total donations are {0:6.2f}, averaging {1:6.2f}\n\n"
        fmtline3 = "Thanks for your ample donation.\n\nRegards,\nThe Staff\n\n"
        outlines.append(fmtline0.format(self.donor_name))
        outlines.append(fmtline1.format(self.last_donation))
        outlines.append(fmtline2.format(self.total_donations,
                                        self.avg_donation))
        outlines.append(fmtline3.format())
        return outlines

    def generate_thankyou(self):
        return '\n'.join(self.generate_text())

    def generate_thankyou_to_file(self):
        outlines = self.generate_text()
        if self.donor_name.count(' ') > 0:
            filename_arg = self.donor_name.replace(' ', '_')
        else:
            filename_arg = self.donor_name
        filename = "./{0}.txt".format(filename_arg)
        print("Writing {0}...".format(filename))
        try:
            with open(filename, 'w') as handle:
                for line in outlines:
                    handle.write(line)
        except PermissionError:
            print("generate_thankyou_to_file: Permission Error")
        except IOError:
            print("generate_thankyou_to_file: I/O Error")
        return filename


class DonorCollection(object):
    """
    DonorCollection class: a collection class with common donor operations
    """
    def __init__(self):
        # dictionary with name as key and donor object as value
        self._donors = {'Bill': Donor('Bill', 100.00)}

    def create_new_donor(self, in_name):
        return Donor(in_name)

    def add_new_donor(self, in_name):
        if in_name in self._donors.keys():
            raise ValueError('name [{0}] already exists'.format(in_name))
        new_donor = self.create_new_donor(in_name)
        self._donors[in_name] = new_donor

    def add_donation(self, in_name, in_donation):
        try:
            self._donors[in_name].add_donation(in_donation)
        except KeyError:
            print('name [{0}] not present in collection'.format(in_name))

    def get_donor(self, in_name):
        donor = None
        try:
            donor = self._donors[in_name]
        except KeyError:
            print('name [{0}] not present in collection'.format(in_name))
        return donor

    def generate_report_all(self):
        outlines = []
        header_fmt_str = "{0:20}{1:10}{2:12}{3:12}"
        hdr1 = header_fmt_str.format('Name', 'Num', 'Total', 'Average')
        hdr2 = header_fmt_str.format('', 'Donations', 'Donations', 'Donation')
        outlines.append(hdr1)
        outlines.append(hdr2)
        for donor in self._donors.values():
            outlines.append(donor.generate_report_row())
        return '\n'.join(outlines)

    def generate_thankyou_all(self):
        for donor in self._donors.values():
            print(donor.generate_thankyou())

    def generate_thankyou_all_to_file(self):
        filenames = []
        for donor in self._donors.values():
            filenames.append(donor.generate_thankyou_to_file())
        return filenames

    def list_names(self):
        lines = []
        for donor_name in self._donors.keys():
            lines.append(donor_name)
        return '\n'.join(lines)
