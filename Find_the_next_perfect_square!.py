'''
You might know some pretty large perfect squares. But what about the NEXT one?

Complete the findNextSquare method that finds the next integral perfect square after the one
passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n)
is also an integer.

If the parameter is itself not a perfect square, than -1 should be returned. You may assume the parameter is positive.

Examples:

findNextSquare(121) --> returns 144
findNextSquare(625) --> returns 676
findNextSquare(114) --> returns -1 since 114 is not a perfect

https://www.codewars.com/kata/56269eb78ad2e4ced1000013/python 

best answer

def find_next_square(sq):
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1)**2
    return -1
'''
from math import sqrt 
# def find_next_square(sq):
#     # Return the next square if sq is a square, -1 otherwise
#     if not sqrt(sq).is_integer(): return -1
#     else:
#         sq+=1
#         while True:
#             if not sqrt(sq).is_integer():sq+=1
#             else: return sq


def find_next_square(sq):
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1)**2
    return -1

num = 121
r = find_next_square(num)
print(r)
