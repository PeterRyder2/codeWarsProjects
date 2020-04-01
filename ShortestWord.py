'''
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.

best answer
def find_short(s):
    return min(len(x) for x in s.split())

'''

#%%
def find_short(s):
    # your code here
    l = s.split(" ")
    shortest = l[0]
    for i in l:
        if len(i) < len(shortest): shortest = i

    return len(shortest) # l: shortest word length

r=  "I am great"
rVal = find_short(r)
rVal