
import sys
import tempfile

user_options = {
    "Send": "Send a Thank You to a single donor",
    "Report": "Create a Report",
    "Letter": "Send a letter to all donors",
    "Quit": "Quit",
}

donor_db = {
    "alex" : [53898.23, 2653.00, 105.07],
    "jeff" : [183.00, 200.00],
    "paul" : [33941.98],
    "mark" : [1.65, 55.00],
    "john" : [2705.71],
}


def sort_key(donor_db):
    return sum(donor_db[1])


def send_thanks():
    name = ''
    while not name or name.lower() == 'list':
        name = input("Please enter the full name: ").lower()
        if name == 'list':
            print(' '.join(donor_db))
    amt = int(input("Please enter the donation amount: "))
    donor_db.setdefault(name,[]).append(amt)

    print(f'\nDear {name.capitalize()},\
        \nThank you for the donation of ${amt:.2f}.\nSincerely,\
        \nThe Mailroom Foundation')


def donor_rpt():
    header = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gift']
    seperator = '-' * 50
    print(f'\n{header[0]:13}|{header[1]:<10}|{header[2]:<10}|{header[3]:<10}\n{seperator}')
    donor_db_sum = {donor: sum(donor_db[donor]) for donor in donor_db}
    key_sort = sorted(donor_db_sum, key=donor_db_sum.__getitem__,reverse=True)
    for donor in key_sort:
        print(f'{donor.capitalize():13}',\
            f'{sum(donor_db.get(donor)):>10.2f}',\
            f'{len(donor_db.get(donor)):>10}',\
            f'${sum(donor_db.get(donor))/len(donor_db.get(donor)):>10.2f}'
        )


def thanks_all():
    path = input("Please enter the path: ")
    if path != '':
        path = path + "\\"
    for donor_key,donor_val in donor_db.items():
        with open("{}{}.txt".format(path, donor_key), "w") as thank_you:
            thank_you.write(f'\nDear {donor_key.capitalize()},\
                \nThank you for the donation of ${sum(donor_db.get(donor_key)):.2f}.\nSincerely,\
                \nThe Mailroom Foundation')

    if path != '':
        print("\n Letters were successfully saved to {}.\n".format(path))
    else:
        print("\n Letters were successfully saved in the current directory.\n")


def exit_program():
    print("Bye!")
    sys.exit()


switch_dict = {
    1 : send_thanks ,
    2 : donor_rpt ,
    3 : thanks_all,
    4 : exit_program,
}


def main():
    main_menu = ("\n Would you like to: \
        \n 1 - {Send}\
        \n 2 - {Report}\
        \n 3 - {Letter}\
        \n 4 - {Quit}\
        \n >>>> ".format(**user_options)
    )
    while True:
        response = int(input(main_menu))
        if response in switch_dict.keys():
            switch_dict.get(response)()
        else:
            print("Warning: Not a valid option!")

if __name__ == "__main__":
    main()