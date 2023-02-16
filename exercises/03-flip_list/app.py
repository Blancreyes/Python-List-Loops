arr = [45, 67, 87, 23, 5,  32, 60]

#your code below:
new_list=[]

start=len(arr)-1

for x in range (start, -1,-1):
    new_list.append(arr[x])

print(new_list)
