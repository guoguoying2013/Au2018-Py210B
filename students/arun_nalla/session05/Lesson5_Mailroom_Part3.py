#!usr/bin/env python

donors_dict = {'Aron King': [1, 2], 'Becky Patty': [3000, 1000], 'Charlie Lee': [666, 222], 'Thomas Dave':[202, 90, 450], 'Nancy Crow': [100, 200, 300]}

def thanks_email():
    while True:
        name_input = input("Enter full name of a donor>>>").title()
        if name_input == 'List': print(list(donors_dict))
        else:
            try:
                donation_amount = int(input('Enter donation amount: '))
                donors_dict.setdefault(name_input, []).append(donation_amount)
                d = {}
                d['name'] = name_input
                d['donation'] = donation_amount
                print("\nDear {name},\n\tThank you for generous donation of ${donation:.2f} to ZYX charity\n"
                      "Sincerely,\nZYX Team".format(**d))
                return

            except ValueError:
                print ('Please enter a value, entry should be an integer.')
                return

def sort_key(sorting):
    return sorting[1]

def create_report():

    list_donors = [[a, sum(donors_dict[a]), len(donors_dict[a]), sum(donors_dict[a])/len(donors_dict[a])] for
                   a in list(donors_dict)]
    list_sorting = (sorted(list_donors, key=sort_key, reverse=True))
    print(list_sorting); print("\nList of donors and Contribution to XYZ Charity\n")
    print("{:<20}\t\t{:<10}\t\t{:<10}\t\t{:<10}".format('Donors-name', 'Total', 'Num gifts', 'Average gift'))
    print('_ ' * 40)
    for a, b, c, d in list_sorting:
        print("{:20}\t\t${:<10.2f}\t\t{:^10}\t\t${:<10.2f}".format(a,b,c,d))
    print('_ ' * 40); print('End of Report\n')


def quit_program():
    print('Thank for using this script.\nHave a nice day\nBye\n')
    exit()

def email_donors():

    for name in donors_dict:
        message = ('Dear {},\n\n\tThank you for your very kind donation of ${:0.2f}.\n\tIt will be put '
                   'to very good use.\n\n\t\tSincerely,\n\t\t-The Team'.format(name, sum(donors_dict[name])))
        try:
            with open ('Mailroom_messages\e_mail_{}.txt'.format(name), 'w') as f:
                f.write(message)

        except FileNotFoundError:
            print ('Check for the file /folder name or path of the directory that stores all the e-mails')
            break

    else:
        print('\nAll e-mails are stored in a folder located in current directory.\n')

dict_list = {"1": thanks_email, "2": create_report, "3": email_donors, "4": quit_program}
def main ():

    while True:
        try:
            response = input("MAIN MENU\nDonors and donations made to XYZ organisation.\nPlease select one of the option"
                         " below to proceed.\n1.Send a Thank you message to the donor\n2.Create a report\n3.Send "
                            "letters to all donors\n4. Quit\n>>>")
            dict_list[response]()
        except KeyError:
            print ("Invalid input.\nPlease select correct option")
        finally:
            print ('Thank You\n\n')

if __name__=="__main__":
    main()
