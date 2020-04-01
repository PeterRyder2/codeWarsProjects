#%%
def reverse(string):
    rString = [string[i-1] for i in range(len(string),0,-1)]
 
    return(''.join([str(elem) for elem in rString]) )
string = "peter"
r = reverse(string)
print(r)


# %%
