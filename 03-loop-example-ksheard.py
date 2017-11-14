#These loop examples will sort a list of the names of my labmates alphabetically and by name length.

#These are the sorted lists with built-in Python functions
labmates = ['Kelsey', 'Rachel', 'Mathili', 'Aditya', 'Courtney', 'Sarah', 'Sully', 'Chaitali', 'Jeremy', 'Darya', 'Izzy']
labmates.sort() #sorts labmembers alphabetically
labmates.sort(key = len) #sorts labmembers by name length
print('There are ', len(labmates), 'members of the Cox and Smyth labs:', labmates)

#Below are my attempts to sort the list with loops

#This nested loop compares two adjacent values in a list throughout the length of the list.
#The initial pair is (i, i+1), and the  larger value of the pair moves throughout the list until a larger value is reached.
#At this index, the existing value is replaced with the larger pair member, and the value being replaced forms a new pair with its i + 1 neighbor.
labmates = ['Kelsey', 'Rachel', 'Mathili', 'Aditya', 'Courtney', 'Sarah', 'Sully', 'Chaitali', 'Jeremy', 'Darya', 'Izzy']
for i in range(len(labmates)): #loops along the length of labmates
    for j in range(len(labmates) - 1): #second loop loops along labmates n-1 since one value is already held
        if labmates[j] > labmates[j+1]: #compares the size of j to its righthand neighbor
            labmates[j+1], labmates[j] = labmates[j], labmates[j+1] #swaps the values of [j] and [j+1] in the list if the conditon above is met
print(labmates)

#This is a generic function for the sorting loop above
labmates = ['Kelsey', 'Rachel', 'Mathili', 'Aditya', 'Courtney', 'Sarah', 'Sully', 'Chaitali', 'Jeremy', 'Darya', 'Izzy']
def sorting(x):
    for i in range(len(x)):
        for j in range(len(x) - 1):
            if x[j] > x[j+1]:
                x[j+1], x[j] = x[j], x[j+1]
labmates.sort() == sorting(labmates) #checks if the loop sorting function returns the same output as the built-in function

labmates = ['Kelsey', 'Rachel', 'Mathili', 'Aditya', 'Courtney', 'Sarah', 'Sully', 'Chaitali', 'Jeremy', 'Darya', 'Izzy']
def length_sorting(x): #slightly modified function which sorts the list by name length
    for i in range(len(x)):
        for j in range(len(x) - 1):
            if len(x[j]) > len(x[j+1]): #compares the length of j to the length of its righthand neighbor
                x[j+1], x[j] = x[j], x[j+1]
labmates.sort(key = len) == length_sorting(labmates)
