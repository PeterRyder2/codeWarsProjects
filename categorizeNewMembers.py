''' 
The Western Suburbs Croquet Club has two categories of membership, Senior and Open. They would like your help with an application form that will tell prospective members which category they will be placed.

To be a senior, a member must be at least 55 years old and have a handicap greater than 7. In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.

Input
Input will consist of a list of lists containing two items each. Each list contains information for a single potential member. Information consists of an integer for the person's age and an integer for the person's handicap.

Note for F#: The input will be of (int list list) which is a List<List>

Example Input
[[18, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9]]
Output
Output will consist of a list of string values (in Haskell: Open or Senior) stating whether the respective member is to be placed in the senior or open category.

Example Output
["Open", "Open", "Senior", "Open", "Open", "Senior"]


'''

#%%
# my answer
# def openOrSenior(data):
#     # to be a senior you need to be 55 and have a handicap >7
#     rList = []

#     for i in range(len(data)):
#             if data[i][0] >= 55 and data[i][1] >  7: rList.append("Senior")
#             else: rList.append("Open") 
        
#     return rList
# data = [[45, 12],[55,21],[19, -2],[104, 20]]

# r = openOrSenior(data)
# r


'''

Best answer 
  return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]

def openOrSenior(data):
    return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]
'''

def openOrSenior(data):
    # to be a senior you need to be 55 and have a handicap >7
    rList = []

    for (age, handicap) in data:
        print (age, handicap)
        if age >= 55 and handicap >  7: rList.append("Senior")

        else: rList.append("Open") 
        
    return rList
data = [[45, 12,34]]

r = openOrSenior(data)
r


