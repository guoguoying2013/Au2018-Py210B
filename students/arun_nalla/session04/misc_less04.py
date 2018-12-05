#!usr/bin/env python
donors_list = [('Aron King', [1,2]), ('Becky Patty',[3000,1000]),
               ('Charlie Lee',[666,222]),('Thomas Dave',[202,90,450]),('Nancy Crow',[100,200,300])]
donors_dict = {x: y for x, y in donors_list}


def list_to_dict(seq):

    d = {}
    for a in donors_dict.keys():
        d['name'] = a
        d['donation'] = sum(donors_dict[a])
        message = "Dear {name}\nThank you for generous donation of ${donation} to ZYX " \
                  "charity\nSincerely\nZYX Team".format(**d)
        print (message)
#list_to_dict(donors_list)

def thanks_email(seq):

    while True:
        name_input = input("Enter full name of a donor>>>").title()
        if name_input == 'List':
            name_list = [x for x in list(donors_dict.keys())]
            print(name_list)

        else:

            for name in donors_dict.keys():
               if name_input == name:
                   d = {}
                   d['name'] = name
                   donation_amount = int(input('Enter donation amount: '))
                   donors_dict[name].append(donation_amount)
                   d['donation'] = sum(donors_dict[name])
                   print("Dear {name}\nThank you for generous donation of ${donation:.2f} to ZYX charity\nSincerely\nZYX Team".format(**d))
                   return


            else:
                d = {}
                d['name'] = name_input
                donation_amount = int(input('Enter donation amount: '))
                donors_dict[name_input] = [donation_amount]
                d['donation'] = sum(donors_dict[name_input])
                #dict_format(seq,name_input)
                print("Dear {name}\nThank you for generous donation of ${donation:.2f} to ZYX charity\nSincerely\nZYX Team".format(**d))
                return

def dict_format(seq, x):

    d = {}

    for name_input in donors_dict.keys():
        d['name'] = x
        d['donation'] = sum(donors_dict[x])

        print ("Dear {name}\nThank you for generous donation of ${donation} to ZYX " \
                      "charity\nSincerely\nZYX Team".format(**d))
thanks_email(donors_dict)
#dict_format(donors_dict)