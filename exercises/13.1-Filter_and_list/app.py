
all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

#Your code go here:
def names (name):
    for x in name:
        if x[0]=="R":
            return name

resulting_names = list(filter(names, all_names))

print(resulting_names)




