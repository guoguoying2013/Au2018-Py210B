#!usr/bin/env python

donors_list = [('Aron King', [1, 2]), ('Becky Patty', [3000, 1000]),
               ('Charlie Lee', [666, 222]), ('Thomas Dave', [202, 90, 450]), ('Nancy Crow', [100, 200, 300])]

donors_dict = {x: y for x, y in donors_list}


def thanks_email(donors_dict):
    while True:
        name_input = input("Enter full name of a donor>>>").title()
        if name_input == 'List':
            print(list(donors_dict))
        else:
            if name_input in donors_dict:
                d = {}
                d['name'] = name_input
                donation_amount = int(input('Enter donation amount: '))
                donors_dict[name_input].append(donation_amount)
                d['donation'] = donation_amount
                print("Dear {name},\n\tThank you for generous donation of ${donation:.2f} to ZYX charity\nSincerely,\nZYX Team".format(**d))
                return
            else:
                d = {}
                d['name'] = name_input
                donation_amount = int(input('Enter donation amount: '))
                donors_dict[name_input] = [donation_amount]
                d['donation'] = donation_amount
                #dict_format(seq,name_input)
                print("Dear {name},\n\tThank you for generous donation of ${donation:.2f} to ZYX charity\nSincerely,\nZYX Team".format(**d))
                return

def sort_key(sorting):
    return sorting[1]

def create_report(donors_dict):

    list_donors = [[a, sum(donors_dict[a]), len(donors_dict[a])] for a in list(donors_dict)]
    list_sorting = (sorted(list_donors, key=sort_key, reverse=True))
    print(list_sorting)
    print("\nList of donors and Contribution to XYZ Charity\n")
    print("{:<20}\t\t{:<10}\t\t{:<10}\t\t{:<10}".format('Donors-name', 'Total', 'Num gifts', 'Average gift'))
    print('_ ' * 40)
    for a, b, c in list_sorting:
        print("{:20}\t\t${:<10.2f}\t\t{:^10}\t\t${:<10.2f}".format(a, b, c, b/c))
    print('_ ' * 40)
    print('End of Report\n')


def quit_program(donors_dict):
    print('Thank for using this script.\nHave a nice day\nBye\n')
    exit()

def email_donors(donors_dict):

    for a in donors_dict:
        message = ('Dear {},\n\n\tThank you for your very kind donation of ${:0.2f}.\n\tIt will be put '
                   'to very good use.\n\n\t\tSincerely,\n\t\t-The Team'.format(a, sum(donors_dict[a])))
        with open ('Mailroom_messages\e_mail_{}.txt'.format(a), 'w') as f:
            f.write(message)

def main (donors_dict):

    while True:
        response = input("MAIN MENU\nDonors and donations made to XYZ organisation.\nPlease select one of the option"
                         " below to proceed.\n1.Send a Thank you message to the donor\n2.Create a report\n3.Send "
                         "letters to all donors\n4. Quit\n>>>")

        dict_list = {"1": thanks_email, "2": create_report, "3": email_donors, "4": quit_program,}
        dict_list.get(response)(donors_dict)


if __name__ == "__main__":
    main(donors_dict)
