#%%
def high_and_low(numbers): 
    numList = [int(s) for s in numbers.split(" ")]
    numList.sort()    
    return f"{numList[len(numList)-1]} {numList[0]}"
    


nums = "37 5 40 -10"
vals =high_and_low(nums)
vals



# %%
