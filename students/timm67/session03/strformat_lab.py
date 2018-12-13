#!/usr/bin/env python3

"""
Tim Meese
Au2018-Py210B
String Formatting Lab
"""

#
# Task One: formatted output
#

tuple_one = ( 2, 123.4567, 10000, 12345.67)
format_str = "file_{0:03d} :  {1:4.2f}, {2:4.2e}, {3:4.2e}"
print(format_str.format(*tuple_one))

#
# Task Two: formatted output (using keywords)
#

format_str_two = "file_{file_num:03d} :  {arg0:4.2f}, {arg1:4.2e}, {arg2:4.2e}"
print(format_str_two.format(file_num=2, arg0=123.4567, arg1=10000, arg2=12345.67))

#
# Task Three: define a function to return a variable length format string
#

def formatter(in_tuple):
    tuple_len = len(in_tuple)
    fmt_string = "The {:d} numbers are: ".format(tuple_len)
    fmt_string += tuple_len * '{:d}, '
    return fmt_string.format(*in_tuple)

tuple_three = (1,2,3,4,5)
a = formatter(tuple_three)
print(a)

#
# Task Four: use format string indeces to reorder input data
#

tuple_four = ( 4, 30, 2017, 2, 27)
fmt_str = "{3:02d} {4:02d} {2:04d} {0:02d} {1:02d}"
print(fmt_str.format(*tuple_four))

#
# Task Five: use fstrings
#

list_five = ['oranges', 1.3, 'lemons', 1.1]
print(f"The weight of an {str(list_five[0]).rstrip('s')} is {list_five[1]} and the weight of a {str(list_five[2]).rstrip('s')} is {list_five[3]}")
print(f"The weight of an {str(list_five[0]).rstrip('s').upper()} is {(list_five[1] * 1.2)} and the weight of a {str(list_five[2]).rstrip('s').upper()} is {(list_five[3] * 1.2)}")

#
# Task Six: print a table with variable size columns
#

data_six = [['1967 Corvette Stingray', 51, 175000.00],
            ['2014 Nissan LEAF', 4, 9000.00],
            ]

fmt_str_six = "{0:30} {1:4d} {2:10.2f}"
fmt_str_six_hdr = "{0:30} {1:4} {2:10}"
print(fmt_str_six_hdr.format('Vehicle', ' Age', ' Value'))
for x in data_six:
    print(fmt_str_six.format(x[0], x[1], x[2]))
