friends = ["Alice", "Bob", "Charlie", "David"]

print(friends[1:3])


# list is a mutable data type in python

# friends[0] = "rohit"
# print(friends)
friends.append("Eve")
print(friends)
ll = [1, 34, 32,43,34,43,54,45]

# ll.sort()
# ll.reverse()
# ll.insert(2, 100) #2 is a index and 100 is a value

# value = ll.pop(2) #2 is a index and it will remove the value at index 2 and return it
ll.remove(43) #43 is a value and it will remove the first occurrence of 43 from the list
# print(value)
print(ll)
