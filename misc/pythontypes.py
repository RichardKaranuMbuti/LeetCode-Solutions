my_data = [
    {
        "name": "Alex",
        "Age": 33,
        "is_active": False
    },
    {
        "name": "Vin",
        "Age": 23,
        "is_active": True
    }

]

print(my_data[0]['name'])
print('True' if 'name' in my_data[0] else 'False'  )

my_tuple = (1, 2, 3)
print(my_tuple[0])  # Output: 1


# Creating a list of tuples
list_of_tuples = [(1, 'a'), (2, 'b'), (3, 'c')]

# Accessing elements
print(list_of_tuples[0])        # Output: (1, 'a')
print(list_of_tuples[0][1])     # Output: 'a'   (Accessing the second element of the first tuple)
print(list_of_tuples[2][0])     # Output: 3     (Accessing the first element of the third tuple)


# Creating a list of sets
list_of_sets = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}]

# Accessing elements
print(list_of_sets[0])          # Output: {1, 2, 3}   (Accessing the first set)
print(2 in list_of_sets[0])     # Output: True       (Checking if 2 is in the first set)

# Accessing individual elements in sets
for elem in list_of_sets[1]:    # Iterating through the second set
    print(elem)                 # Output: 4, 5, 6 (order may vary since sets are unordered)
