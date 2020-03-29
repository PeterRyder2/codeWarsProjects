''' 
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

For example:

 persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
                       # and 4 has only one digit.

 persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
                       # 1*2*6 = 12, and finally 1*2 = 2.

 persistence(4) => 0   # Because 4 is already a one-digit number.
 persistence(39) # returns 3, because 3*9=27, 2*7=14, 1*4=4
                 # and 4 has only one digit

 persistence(999) # returns 4, because 9*9*9=729, 7*2*9=126,
                  # 1*2*6=12, and finally 1*2=2

 persistence(4) # returns 0, because 4 is already a one-digit number


Test.it("Basic tests")
Test.assert_equals(persistence(39), 3)
Test.assert_equals(persistence(4), 0)
Test.assert_equals(persistence(25), 2)
Test.assert_equals(persistence(999), 4)

https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python

'''
#%%
# my attempt
from functools import reduce 
def persistence(n):
    if len(str(n)) == 1: return 0
    #base case
    count = 0
    while True:
        intList = [int(i) for i in str(n)]
        count +=1
        n = reduce((lambda x, y: x * y), intList)
        if len(str(n)) == 1: return count 

num = 4
result = persistence(num)
print (result)


# %%
