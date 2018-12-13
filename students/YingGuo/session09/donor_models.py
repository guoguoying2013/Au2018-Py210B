#!/usr/bin/env python3

class Donor:
    def __init__(self, name, initial_donation=None):
        self.__name = name
        self.__donations = []
        if initial_donation is not None:
            self.__donations.append(initial_donation)
    
    @property
    def name(self):
        return self.__name
    
    @property
    def donation(self):
        return self.__donations
    
    @property
    def num_donations(self):
        return len(self.__donations)
    
    @property
    def total_donations(self):
        return sum(self.__donations)
    
    @property
    def avg_donation(self):
        return self.total_donations/self.num_donations

    #you can call instance.__dict__ to view this information 
    def __str__(self):
        return "[Donor name = {}, donations = {}]".format(self.__name, self.__donations)

    #__is not directly viewed from outside, make attribute invisible from outside
    def add_donation(self, donation):
        self.__donations.append(donation)

    #generate report row
    def generate_report_row(self):
        return "|{:>12}|{:>12}|{:>12}|{}|".format(self.__name, self.total_donations, self.avg_donation, self.__donations)

    def thank_you(self):
        message = "Dear {},\n Thank you for your donation of {}!\n".format(self.__name, self.__donations)
        print(message)
        return(message)


class DonorCollection:
    def __init__(self):
        self.__donors = {} #name: Donor pairs

#why we use __ ??hidden, access via method
    def add_new_donor(self,name):
        if name in self.__donors:
            raise ValueError("name({}) already exists".format(name))
        self.__donors[name] = Donor(name)
    
    def add_donation(self,name,donation):
        self.__donors[name].add_donation(donation)
    
    def get_donor(self,name):
        return self.__donors[name]
    
    def generate_report(self):
        header = "|{:>12}|{:>12}|{:>12}|{:>12}|".format("Name","Total", "Average", "# donations")
        lines = [header]
        #values(), donor object, an instance of donor class
        for donor in self.__donors.values():
            lines.append(donor.generate_report_row())
        return "\n".join(lines)
    
    def thank_you_letter(self):
        for donor in self.__donors.values():
            donor.thank_you()

    def write_to_file(self):
        for name in self.__donors.keys():
            with open(name,"w") as f:
                f.write(self.__donors[name].thank_you())

if __name__ == "__main__":
    dc = DonorCollection()
    dc.add_new_donor("Bill")
    dc.add_donation("Bill",1234)
    dc.add_donation("Bill",5678)
    dc.add_new_donor("Paul")
    dc.add_donation("Paul",1000)
    dc.generate_report()
    dc.thank_you_letter()
