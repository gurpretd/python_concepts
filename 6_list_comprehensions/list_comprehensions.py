# Do square of elements the original list.
import random

old_list = [1, 2, 3, 4, 5]
new_list = [x * x for x in old_list]
print(new_list)

# Find len of each word of list
str_list = ["apple", "banana", "kiwi", "strawberry"]
str_len = [len(x) for x in str_list]
print(str_len)

# *** Adding Conditions to List Comprehensions
# Find odd elements of the list
old_list = [11, 22, 33, 44, 55, 66, 77, 88]
even_list = [x for x in old_list if x % 2 == 0]
print(even_list)
odd_list = [x for x in old_list if x % 2 != 0]
print(odd_list)

# Adding else statement too.
#So here we return even numbers from list. And return zero for odd numbers.
old_list = [11, 22, 33, 44, 55, 66, 77, 88]
even_list = [x if x % 2 == 0 else 0 for x in old_list]
print(even_list)


# Nested list comprehensions
# Create 3x3 matrix

matrix = [[i*2, i*2+1, i*2+2] for i in range(3)]
print(matrix)

# Do square of elements the original list with lambda.
old_list = [1, 2, 3, 4, 5]
new_list = [(lambda x: x*x)(x) for x in old_list]
print(new_list)


# Find len of each word of list with lambda
str_list = ["apple", "banana", "kiwi", "strawberry"]
str_len = [(lambda word:len(word))(word) for word in str_list]
print(str_len)


#So here we return even numbers from list. And return zero for odd numbers.
old_list = [11, 22, 33, 44, 55, 66, 77, 88]
new_list = [(lambda x: x if x%2 == 0 else 0)(x) for x in old_list]
print(new_list)





