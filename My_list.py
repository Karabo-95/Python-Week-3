# Create an empty list called my_list
my_list = []

# Append the following elements to my_list: 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert the value 15 at the second position in the list
my_list.insert(1, 15)  # Insert 15 at index 1 (second position)

# Extend my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])

# Remove the last element from my_list
my_list.pop()  # Removes the last element (70)

# Sort my_list in ascending order
my_list.sort()

# Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)  

# Find the index of 30
print(f"The index of 30 in my_list is: {index_of_30}")

# Final list output (optional)
print("Final my_list:", my_list)
