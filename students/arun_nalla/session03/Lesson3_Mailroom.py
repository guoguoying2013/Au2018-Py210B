#!usr/bin/env python
donors_list = [('Aron King', [1,2]), ('Becky Patty', [3000,1000]), ('Charlie Lee', [666,222]), ('Thomas Dave',[202,90,450]), ('Nancy Crow',[100,200,300])]

def thanks_email(seq):
    while True:
        name_input = input("Enter full name of a donor>>>").title()
        if name_input == 'List':
            name_list = [x for x, y in seq]
            print(name_list)
        else:
            for i, v in enumerate(seq):
                if name_input == seq[i][0]:
                    donation_amount = float(input('Enter donation amount: '))
                    seq[i][1].append(donation_amount)
                    print("Dear {},\n\nThis message is regarding the recent donation of ${:.2f} you made to "
                          "ZYX charity.\nWe highly appreciate your kindness. Till date you have donate a total of"
                          " ${:.2f}.\n\nWith Regards\n\nXYZ\n".format(name_input, donation_amount, sum(seq[i][1])))
                    return seq
            else:
                donation_amount = float(input('Enter donation amount: '))
                seq.append((name_input, [donation_amount]))
                print("Dear {},\nThis message is regarding the recent donation of ${:.2f} you made to ZYX charity.\n"
                    "We highly appreciate your kindness and making a contribution.\n\n"
                    "With Regards\n\nXYZ\n".format(name_input, donation_amount))
                return seq

def sort_key(sorting):
    return sorting[1]
def create_report(seq):
    list_sort = [(x,sum(y),len(y)) for x,y in seq]
    list_sorting = (sorted(list_sort,key=sort_key,reverse = True))
    print (list_sorting)
    print ("\nList of donors and Contribution to XYZ Charity\n")
    print ("{:<20}\t\t{:<10}\t\t{:<10}\t\t{:<10}".format('Donors-name','Total','Num gifts', 'Average gift'))
    print ('_ '*40)
    for a,b,c in list_sorting:
        print ("{:20}\t\t${:<10.2f}\t\t{:^10}\t\t${:<10.2f}".format(a,b,c,b/c))
    print('_ ' * 40)
    print ('End of Report\n')

def quit_program():
    print ('Thank for using this script.\nHave a nice day\nBye\n')
    exit()
def main (seq):
    while True:
        response = input("MAIN MENU\nDonors and donations made to XYZ organisation.\nPlease select one "
                         "of the option below to proceed.\n1.Send a Thank you message to the donor\n2.Create a "
                         "report\n3. Quit\n>>>")  # continuously collect user selection
        # now redirect to feature functions based on the user selection
        if response == "1":
            thanks_email(seq)
        elif response == "2":
            create_report(seq)
        elif response == "3":
            quit_program()
            break
        else:
            print("Not a valid option!")

if __name__ == "__main__":
    main(donors_list)
