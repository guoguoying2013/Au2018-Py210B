#!/usr/bin/env python3
"""
Tim Meese
Au2018-Py210B
Slice Demo
"""

def slice_exchange_first_last(seq):
    firstElement = seq[0]
    lastElement = seq[-1]
    seq[0] = lastElement
    seq[len(seq)-1] = firstElement
    return seq

def slice_rm_ev_other(seq):
    sliceObj = slice(0, -1, 2)
    return seq[sliceObj]

def slice_rm_ev_other_after_1st_4_last_4(seq):
    if (len(seq)< 8):
        raise Exception("List too short")
    front_slice = seq[-4:]
    print("{}".format(front_slice))
    front_back_slice = front_slice[:-4]
    print("{}".format(front_back_slice))
    sliceObj = slice(0, -1, 2)
    return front_back_slice[sliceObj]
    
def slice_reverse_seq(seq):
    # NOTE: In Python 3, use two forward slashes for floor (integer) division
    for x in range(0, (len(seq)//2)):
        temp = seq[((len(seq) - 1) - x)]
        seq[((len(seq) - 1) - x)] = seq[x]
        seq[x] = temp
    return seq

def slice_last_third_first_third_mid_third_new_order(seq):
    return seq

def print_menu():
    print("Slice Demo")
    print("[1] Exchange first and last element of set")
    print("[2] Remove every other element of set")
    print("[3] Remove every other element of set after 1st 4 and last 4 items removed")
    print("[4] Reverse the order of sequence using only slice")
    print("[5] Last third, first third, mid third in new order") 
    print("[9] Exit Demo")
    pass

def main():

    exitDemo = False
    while(exitDemo == False):
        print_menu()
        response = input("Enter Option: ")
        try:
            response = int(response)
        except(ValueError):
	        print("Enter a number between 1-9")
	        continue
        if (response == 9):
            exitDemo = True
        elif (response == 5):
            orig_seq5 = [0,1,2,3,4,5,6,7,8]
            ret_seq5 = slice_last_third_first_third_mid_third_new_order(orig_seq5)
            print("{}".format(ret_seq5))
            pass
        elif (response == 4):
            orig_seq4 = [0,1,2,3]
            ret_seq4 = slice_reverse_seq(orig_seq4)
            print("{}".format(ret_seq4))
            pass
        elif (response == 3):
            orig_seq3=[0,1,2,3,4,5,6,7,8,9,10,11,12]
            ret_seq3 = slice_rm_ev_other_after_1st_4_last_4(orig_seq3)
            print("{}".format(ret_seq3))
            pass
        elif (response == 2):
            orig_seq2 = [0,1,2,3]
            ret_seq2 = slice_rm_ev_other(orig_seq2)
            print("{}".format(ret_seq2))
            pass
        elif (response == 1):
            orig_seq1 = [0,1,2,3]
            ret_seq1 = slice_exchange_first_last(orig_seq1)
            print("{}".format(ret_seq1))
            pass
        else:
            print("Invalid response entered\n")

if __name__ == "__main__":
    main()
