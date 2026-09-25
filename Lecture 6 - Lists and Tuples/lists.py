empty_lst = []
# empty_lst = list()
print(empty_lst)
print(type(empty_lst))

numbers = [1, 2, 3, 4, 5]
print(numbers)

names = ["John", "Anna", "Bob"]
print(names)

mixed_lst = [1, "Python", 3.14, True, False, 20]
print(mixed_lst)


lst = [1, 2, 3, 4, 5, 6, 9, 8, 7, 10]

print(lst[0])
print(lst[-1])
print(lst[2])
print(lst[10])

print(lst[0:5])
print(lst[5:])
print(lst[:5])
print(lst[::2])
print(lst[::-1])

# strings are immutable
name = "Nini"
print(id(name))
name = name.lower()
print(id(name))


# lists are mutable
fruits = ["apple", "cherry", "orange", "banana"]
print(fruits)
print(id(fruits))

fruits[0] = "kiwi"
print(fruits)
print(id(fruits))


###############################
# Adding Items
###############################

nums = [1, 2, 3]
nums.append("Python")
print(nums)

nums.insert(0, "Hello")
print(nums)

nums1 = [4, 5, 6]
nums.extend(nums1)
nums.extend([6, 7, 8])
print(nums)
print(nums1)



###############################
# Deleting Items
###############################

fruits = ["Apple", "Banana", "Orange"]
print(fruits)
fruits.remove("Banana")
print(fruits)

removed_items = fruits.pop()
print(fruits)
print(removed_items)

fruits.clear()
print(fruits)

del fruits
print(fruits)



##################################
# List Methods
##################################

nums = [1, 2, 3, 10, 9, 7, 3, 11]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(nums.count(3))
print(nums.index(2))

nums.sort()   # ascending
print(nums)

nums.sort(reverse=True) # descending
print(nums)

nums.reverse()
print(nums)


nums = sorted(nums)
print(nums)

nums = sorted(nums, reverse=True)
print(nums)


##################################
# Shallow Copy
##################################

a = [1, 2, 3]
b = a
print(id(a))
print(id(b))

b.append(4)
print(b)
print(a)



##################################
# Deep Copy
##################################


import copy

a = [1, 2, 3]
b = copy.deepcopy(a)
print(a)
print(b)
print(id(a))
print(id(b))

b.append(4)
print(b)
print(a)


numbers[1] = 10
print(numbers)



#####################################
# For Loop in Lists
#####################################


fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

lst = []

for i in range(1, 11):
    lst.append(i)

print(lst)


####################################
# List Comprehension
####################################

lst = [i for i in range(1, 11)]
print(lst)

lst = [i ** 2 for i in range(1, 11)]
print(lst)