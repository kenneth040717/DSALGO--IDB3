myArray = [23,89, 7, 56, 44]
print("This is the initial order of the Array: ")
print(myArray)

#bubble sort
n = len(myArray) #5 returned value of len()
for i in range(n): # cycles through values 1 -4
    for j in range(0, n - i -1): # cycles through pairs of elements
        if myArray[j] > myArray[j+1]:
            myArray[j], myArray[j+1] = myArray[j+1], myArray[j]

print("The sorted array using Bubble sort ascending: ")
print(myArray)



#insertion sort
myArray2 = [12, 78, 91, 34, 62]
print("I am printing the unsorted Array: ")
print(myArray2)
#insertion sort proper

for i in range(1, len(myArray2)):
    key = myArray2[i]
    j = i - 1
    # move elements that are greater than the key
    # to one position ahead of
    # their current position

    while j >= 0 and key < myArray2[j]:
        myArray2[j + 1] = myArray2[j]
        j-=1
    myArray2[j + 1] = key
print("The sorted array using the insertion sort ascending: ")
print(myArray2)

#selection sort
myArray3 = [5, 99, 48, 15, 67]
print("I am printing the unsorted Array: ")
print(myArray3)

# Algorithm proper
for i in range(len(myArray3)):
    max_idx = i  # Start with the first element as the maximum
    for j in range(i + 1, len(myArray3)):
        if myArray3[j] > myArray3[max_idx]:  # Change to '>' for descending order
            max_idx = j
    # Swap the found maximum element with the first element
    myArray3[i], myArray3[max_idx] = myArray3[max_idx], myArray3[i]

print("The sorted array using Selection sort Descending: ")
print(myArray3)



#insertion sort descending

myArray4 = [12, 78, 91, 34, 62]
print("I am printing the unsorted Array: ")
print(myArray4)

# Insertion sort for descending order
for i in range(1, len(myArray4)):
    key = myArray4[i]
    j = i - 1
    # Move elements that are less than the key to one position ahead
    while j >= 0 and key > myArray4[j]:  # Change the condition here
        myArray4[j + 1] = myArray4[j]
        j -= 1
    myArray4[j + 1] = key

print("The sorted array using the insertion sort in descending order: ")
print(myArray4)


