#!/usr/bin/env python3

"""
Tim Meese
Au2018-Py210B
Dictionary Lab
"""

#
# Dictionaries 1
#

cakeDict = {'name' : 'Chris', 'city':'Seattle', 'cake':'Chocolate'}
print(cakeDict)
print("Remove cake item...")
cakeDict.popitem()
print(cakeDict)
print("Add fruit item...")
cakeDict['fruit'] = 'Mango'
print(cakeDict)
print("Dict keys: ",end='')
for k in cakeDict.keys():
    print("{}, ".format(k),end='')
print("\nDict values: ",end='')
for item in cakeDict.values():
    print("{}, ".format(item),end='')
print('')
if 'cake' in cakeDict.keys():
    print("cake is a key")
else:
    print("cake is NOT a key")
if 'Mango' in cakeDict.values():
    print("Mango is a value")
else:
    print("Mango is NOT a value")

#
# Dictionaries 2
#

cakeDict = {'name':0, 'city':0, 'cake':0}
for cakeDict.keys