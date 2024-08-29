myArray1 = [23, 89, 7, 56, 44]
myArray2 = [12, 78, 91, 34, 62]
myArray3 = [5, 99, 48, 15, 67]
myArray4 = [12, 78, 91, 34, 62]

# Combine all arrays into one
combined_array = myArray1 + myArray2 + myArray3 + myArray4

# Sorting the combined array using Selection Sort
for i in range(len(combined_array)):
    min_idx = i
    for j in range(i + 1, len(combined_array)):
        if combined_array[min_idx] > combined_array[j]:
            min_idx = j
    combined_array[i], combined_array[min_idx] = combined_array[min_idx], combined_array[i]

# Printing the sorted combined array
print("The sorted combined array using Selection sort:")
print(combined_array)

# Printing even and odd values
even_values = [num for num in combined_array if num % 2 == 0]
odd_values = [num for num in combined_array if num % 2 != 0]

print("Even values:", even_values)
print("Odd values:", odd_values)
