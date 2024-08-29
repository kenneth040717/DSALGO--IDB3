# Separeted Arrays
myArray2 = [12, 78, 91, 34, 62]
myArray3 = [5, 99, 48, 15, 67]

# Insertion Sort for ascending order
sorted_insertion = []
for i in range(1, len(myArray2)):
    key = myArray2[i]
    j = i - 1
    while j >= 0 and key < myArray2[j]:
        myArray2[j + 1] = myArray2[j]
        j -= 1
    myArray2[j + 1] = key
sorted_insertion = myArray2

# Selection Sort for descending order
sorted_selection = []
for i in range(len(myArray3)):
    max_idx = i
    for j in range(i + 1, len(myArray3)):
        if myArray3[j] > myArray3[max_idx]:
            max_idx = j
    myArray3[i], myArray3[max_idx] = myArray3[max_idx], myArray3[i]
sorted_selection = myArray3

# Output the sorted arrays
print("Sorted array using Insertion Sort (Ascending): ", sorted_insertion)
print("Sorted array using Selection Sort (Descending): ", sorted_selection)
