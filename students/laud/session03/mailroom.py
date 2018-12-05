#!/usr/bin/env python3
import sys

""" Historical donations data """
donations = [
    ("Bill Gates", [653772.32, 12.17]),
    ("Jeff Bezos", [877.33]),
    ("Paul Allen", [663.23, 43.87, 1.32]),
    ("Mark Zuckerberg", [1663.23, 4300.87, 10432.00]),
]

""" Available actions """
main_menu = "\n".join(("Welcome!",
          "Please select one of the following options:",
          "1 - Send a Thank You",
          "2 - Create a Report",
          "3 - quit",
          ">>> "))

""" Helper functions """ 
def get_average(donations):
    result = sum(donations)/len(donations)
    return str(round(result, 2))

def get_total(donations):
    result = sum(donations)
    return str(round(result, 2))

def get_count(donations):
    return str(len(donations))

def get_donor_list():
    global donations
    donors = ''
    for x,y in donations:
        donors += x + "\n"
    return donors

def get_donor_data():
    global donations
    donors = []
    for x,y in donations:
        donors.append(x.title())
    return donors

def update_donor_data(name):
    global donations
    yes_no = input("This person is not on your list. Would you like to add them? (y/n) >>>")
    if yes_no.lower() == 'y':
        print()
        amount_input = input("Great! How much is this person donating today (just the amount)? >>>")
        try:
            amount = int(amount_input)
        except ValueError:
            amount == ''
        if amount == '':
            amount_input = input("Please enter a valid amount >>>")
        else:
            print("Thanks! Updating donor data now...")
            new_record = (str(name), [amount])
            donations.append(new_record)
            print()
            print("Donations table updated successfully!")
            print()
            create_report(donations)
            print()
            get_main_menu()
            print()
            print("What else would you like to do today?")
            print()
    elif yes_no.lower() == 'n':
        print()
        print("No worries. Please make a new entry then:")
        send_thank_you()
        print()
    else:
        print()
        print("Invalid entry. Please answer 'y' or 'n':")
        update_donor_data(name)
    return None


def send_mail(name):
    """ Compose and send email """
    message = "\n".join(("Hi " + name +"!",
    "Thank you for your recent donation to our organization.",
    "We appreciate your partnership and look forward to many more opportunities to make a difference together!"))
    print("Sending mail to " + name + "...")
    print()
    print(message)
    print()
    print("Message sent successfully! What else would you like to do today? >>>")
    print()
    get_main_menu()
    print()


def get_main_menu():
    """ Get selected option & call appropriate method """
    global donations
    selected = input(main_menu)

    try:
        choice = int(selected)
    except ValueError:
        choice = ''
    
    if choice == '':
        print()
        print("Oops! Please enter a number from the options.")
        print()
        get_main_menu()
    else:
        if   choice == 1: send_thank_you()
        elif choice == 2: create_report(donations)
        elif choice == 3: quit_program()
        else:
            print("Oops! Please make a valid selection.")
            print()
            get_main_menu()


def send_thank_you():
    """ Send thank you note """
    donors = get_donor_data()
    donor_list = get_donor_list()
    sub_menu = input(
        "Type a donor's Full Name to send a 'Thank You' note. \n"
        "or type 'List' to see a list of donors \n"
        "or type 'Main' to go back to the main menu \n"
        "or type 'Quit' to exit the program >>> \n"
        )
    try:
        entry = sub_menu
    except ValueError:
        entry == ''

    if entry == '':
        print("Oops! Please make an entry")
        send_thank_you()
    else:
        choice = entry.strip()
        if len(choice.split()) > 1:
            new_name = True
            choice = choice.title()
        else:
            new_name = False
            choice = choice
        if choice in donors:
            print()
            send_mail(choice)
            print()
            print("What else would you like to do today?")
            print()
            send_thank_you()
        elif (choice not in donors and new_name):
            print()
            update_donor_data(choice)
        elif choice == 'list':
            print()
            print("Here's your list of donors:")
            print()
            print(donor_list)
            print()
            print("What else would you like to do today?")
            print()
            send_thank_you()
        elif choice == 'main':
            print()
            get_main_menu()
            print()
        elif choice == 'quit':
            print()
            quit_program()
        else:
            print()
            print("Error. Please make a valid entry.")
            print()
            send_thank_you()


def create_report(donations):
    global count
    global average
    header = '{:27}{:10}{:15}{:10}'.format("Donor Name", "Total Given | ", "Num Gifts | ", "Average Gift")
    border = '{:75}'.format("-"*75)
    table = header + "\n" + border + "\n"
    for x,y in donations:
        name = '{:27}'.format(x)
        total = '{:10}'.format( '$' + get_total(y).rjust(10) )
        count = '{:15}'.format( get_count(y).rjust(13) )
        average = '{:10}'.format( '$' + get_average(y).rjust(20) )
        columns = [name, total, count, average]
        table += ('{}'*len(columns)).format(*columns)+ "\n"
    print()
    print("Here's your current donations data:")
    print()
    print(table)
    print()
    print("What else would you like to do today?")

def quit_program():
    return sys.exit("Exiting program. Goodbye...")

""" Initialize the program """
def main():
    while True:
        return get_main_menu()


if __name__ == "__main__":
    main()