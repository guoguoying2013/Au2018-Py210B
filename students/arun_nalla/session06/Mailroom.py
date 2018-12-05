#!usr/bin/env python
""" Mailroom_Part4 assignment - Refracted for unit testing using Pytest"""
import os

donors_dict = {'Aron King': [1, 2], 'Becky Patty': [3000, 1000], 'Charlie Lee': [666, 222], 'Thomas Dave':[202, 90, 450], 'Nancy Crow': [100, 200, 300]}

def donors_list (donors_dict):
    return list(donors_dict)


def add_donors(name, donors_dict):
    return donors_dict.setdefault(name,[])


def add_donation(name, donors_dict, donation):
    add_donors(name, donors_dict).append(donation)
    return donors_dict


def thanks_email():
    while True:
        name_input = input("Enter full name of a donor>>>").title()
        if name_input == 'List': print (donors_list(donors_dict))
        else:
            while True:
                try:
                    donation_amount = int(input('Enter donation amount: '))
                    if donation_amount <= 0:
                        raise ValueError
                    add_donation(name_input, donors_dict, donation_amount)

                    print (email_message(name_input, donation_amount))
                    return
                except ValueError:
                    print ('Please enter a value, entry should be an integer.')


def sort_key(sorting):
    return sorting[1]


def get_report(donors_dict):
    list_donors = ((name, sum(donors_dict[name]), len(donors_dict[name]), sum(donors_dict[name])/len(donors_dict[name]))
                   for name in donors_dict)
    list_sorting = (sorted(list_donors, key=sort_key, reverse=True))
    return list_sorting

    
def create_report():
    header = ("{:<20}{:<15}{:<15}{:^15}".format('Donors-name', 'Total', 'Num. gifts', 'Average Gift'))
    print (header)
    print('_' * len(header))
    for name, donations, num, average in get_report (donors_dict):
        print("{:<20} ${:<15.2f}{:<15}${:<15.2f}".format(name, donations, num, average))
    print('_' * len(header)); print('End of Report\n')


def quit_program():
    print('Thank for using this script.\nHave a nice day\nBye\n')
    exit()


def path_to_store(name):
    my_path = os.path.join(os.getcwd(), 'Mailroom')
    return os.path.join(my_path, 'email_{}.txt'.format(name))


def email_message (name, donation):
    return ("Dear {},\nThank you for generous donation of ${:.2f}. It will be put to a good cause.\nSincerely,"
            "\nThe Team".format(name, donation))


def store_emails():
    for name in donors_dict:
        try:
            with open(os.path.join(path_to_store(name)), 'w') as f:
                f.write(email_message(name, sum(donors_dict[name])))

        except FileNotFoundError:
            print ('Check for the file /folder name or path of the directory that stores all the e-mails')
            break
    else:
        print('\nAll e-mails are stored in current directory.\n')


dict_list = {"1": thanks_email, "2": create_report, "3": store_emails, "4": quit_program}


def main ():
    while True:
        try:
            response = input("MAIN MENU\nDonors and donations made to XYZ organisation.\nPlease select one of the "
                             "option below to proceed.\n1.Send a Thank you message to the donor\n2.Create a report\n"
                             "3.Send letters to all donors\n4. Quit\n>>>")
            dict_list.get(response)()
        except TypeError:
            print ("Invalid input.\nPlease select correct option")
        finally:
            print ('Thank You\n\n')


if __name__ == "__main__":
    main()
