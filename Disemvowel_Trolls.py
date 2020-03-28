'''
Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata y isn't considered a vowel.


'''
#%%
def disemvowel(string):
    returnString =""
    vowels = ["a","e", "i", "o", "u"]
    upperVowels = ["A", "E", "I", "O", "U"]
    vowless = [i for i in string if i not in vowels and i not in upperVowels]
    for letters in vowless:
        returnString += letters

    return returnString

string = "hEllo"
dis = disemvowel(string)
dis



#%%
def disemvowel(s):
    return s.translate(None,  "aeiouAEIOU")

e = "Hello"
i = disemvowel(e)
i
# %%
