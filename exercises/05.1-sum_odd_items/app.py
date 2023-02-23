arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:
def sum_odds(items):

    total= 0
    #The magic happens here:
    for items in arr:
        if items % 2 != 0:
            total+=items
    return total
    
print(sum_odds(arr))




