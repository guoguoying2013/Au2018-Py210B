#! usr/bin/env python
nums = list(range(1,101))

for num in nums:
    if num%3 == 0 and num%5!=0:
        print ('Fizz')
    elif num%5 ==0 and num%3!=0:
        print ('Buzz')
    elif num%3==0 and num%5==0:
        print ('FizzBuzz')
    else:
        print (num)
print ()      
print ('Done')
