#!/usr/bin/env python3

from donor_models import *

if __name__ == "__main__":
    dc = DonorCollection()
    while True:
        try:
            user_input = int(input("\
            1. add new donor\n\
            2. add donation to existing donor\n\
            3. full report\n\
            4. send thank you\n\
            5. quit"))

            if user_input == 1:
                input_name = input("What's the name of new donor?")
                dc.add_new_donor(input_name)
                print(dc.__init__())
            
            if user_input == 4:
                print(dc.thank_you_letter())
            
            if user_input == 2:
                input_name2 = input("what's the name?")
                input_donation = int(input("how much would you like to donate?"))
                dc.add_donation(input_name2, input_donation)
            
            if user_input == 3:
                print(dc.generate_report())
            
            if user_input == 5:
                break

        except (TypeError, ValueError):
            print("please pick from 1 to 5")