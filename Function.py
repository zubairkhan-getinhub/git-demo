
# def reverse_string(s):
#     return s[::-1]

# print(reverse_string("hello"))

# def reverse_string(s):
#     print(s[::-1]) 
# reverse_string("ZUBAIR")

# # Check if a string is a palindrome.

# # bismillah
# def is_palindrome(s):
#     return s == s[::-1]

# print(is_palindrome("racecar"))

# def is_palindrom(s):
#     print(s == s[::-1])
# is_palindrom("racecar")
# # Count the number of vowels in a string.


# def count_vowels(s):
#     vowels = "aeiouAEIOU"
#     return sum(1 for char in s if char in vowels)

# print(count_vowels("AEIOU"))

# def count_vowels(s):
#     count = 0
#     vowels = "AEIOUaeiou"
#     for chr in s:
#         if chr in vowels:
#             count = count + 1
#     print(count)
# count_vowels("aeiou AEIOU")

# Remove all vowels from a string.


# def remove_vowels(s):
#     vowels = "aeiouAEIOU"
#     return "".join(char for char in s if char not in vowels)

# print(remove_vowels("hello world"))

# def remove_vowels(s):
#     vowels = "aeiouAEIOU"
#     return "".join(char for char in s if char not in vowels)

# print(remove_vowels("hello world"))


# # Find the length of the longest word in a string.


# def longest_word_length(s):
#     words = s.split()
#     print( s.split())
    

#     return max(len(word) for word in words)

# print(longest_word_length("The quick brown fox jumps over the lazy dog"))
# # Lists
# # Find the maximum number in a list.
# # bismillah
# def find_max(lst):
#     return max(lst)

# print(find_max([1, 2, 3, 4, 5]))
# # Find the minimum number in a list.


# def find_min(lst):
#     return min(lst)

# print(find_min([1, 2, 3, 4, 5]))
# # Calculate the sum of all numbers in a list.
# # bismillah
# def calculate_sum(lst):
#     return sum(lst)

# print(calculate_sum([1, 2, 3, 4, 5]))
# # Calculate the product of all numbers in a list.
# # bismillah
# from functools import reduce

# def calculate_product(lst):
#     return reduce(lambda x, y: x * y, lst)

# print(calculate_product([1, 2, 3, 4, 5]))
# # Find the average of all numbers in a list.


# def calculate_average(lst):
#     return sum(lst) / len(lst)

# print(calculate_average([1, 2, 3, 4, 5]))
# # Remove all duplicates from a list.


# def remove_duplicates(lst):
#     return list(set(lst))

# print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
# # Check if a list is sorted in ascending order.


# def is_sorted(lst):
#     return lst == sorted(lst)

# print(is_sorted([1, 2, 3, 4, 5]))
# # Find the intersection of two lists.

# # bismillah
# def find_intersection(lst1, lst2):
#     return list(set(lst1) & set(lst2))

# print(find_intersection([1, 2, 3], [3, 4, 5]))
# # Find the union of two lists.


# def find_union(lst1, lst2):
#     return list(set(lst1) | set(lst2))

# print(find_union([1, 2, 3], [3, 4, 5]))
# # Flatten a nested list.


# def flatten(lst):
#     flat_list = []
#     for item in lst:
#         if isinstance(item, list):
#             flat_list.extend(flatten(item))
#         else:
#             flat_list.append(item)
#     return flat_list

# print(flatten([1, [2, [3, 4], 5], 6]))
# # Dictionaries
# # Merge two dictionaries.
# # bismillah
# def merge_dicts(dict1, dict2):
#     merged_dict = dict1.copy()
#     merged_dict.update(dict2)
#     return merged_dict

# print(merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4}))
# # Invert a dictionary (swap keys and values).
# # bismillah
# def invert_dict(d):
#     return {v: k for k, v in d.items()}

# print(invert_dict({"a": 1, "b": 2, "c": 3}))
# # Get the keys of a dictionary as a list.
# # bismillah
# def get_keys(d):
#     return list(d.keys())

# print(get_keys({"a": 1, "b": 2, "c": 3}))
# # Get the values of a dictionary as a list.

# # bismillah
# def get_values(d):
#     return list(d.values())

# print(get_values({"a": 1, "b": 2, "c": 3}))
# # Get the key-value pairs of a dictionary as a list of tuples.
# # bismillah
# def get_items(d):
#     return list(d.items())

# print(get_items({"a": 1, "b": 2, "c": 3}))

# # Add an element to a set.
# # bismillah
# def add_to_set(s, element):
#     s.add(element)
#     return s

# print(add_to_set({1, 2, 3}, 4))
# # Remove an element from a set.
# # bismillah
# def remove_from_set(s, element):
#     s.discard(element)  # Use discard to avoid KeyError if element is not in the set
#     return s

# print(remove_from_set({1, 2, 3}, 2))
# # Check if a set is a subset of another set.
# # bismillah
# def is_subset(s1, s2):
#     return s1.issubset(s2)

# print(is_subset({1, 2}, {1, 2, 3}))
# # Check if a set is a superset of another set.
# # bismillah
# def is_superset(s2, s1):
#     return s2.issuperset(s1)

# print(is_superset({1, 2, 3}, {1, 2}))
# # Find the difference between two sets.
# # bismillah
# def find_difference(s1, s2):
#     return s1.difference(s2)

# print(find_difference({1, 2, 3}, {2, 3, 4}))
# # Convert a list to a tuple.
# # bismillah
# def list_to_tuple(lst):
#     return tuple(lst)

# print(list_to_tuple([1, 2, 3]))
# # Convert a tuple to a list.
# # bismillah
# def tuple_to_list(tp):
#     return list(tp)

# print(tuple_to_list((1, 2, 3)))
# # Check if an element exists in a tuple.
# # bismillah
# def element_in_tuple(t, element):
#     return element in t

# print(element_in_tuple((1, 2, 3), 2))
# # Find the index of an element in a tuple.


# def index_in_tuple(t, element):
#     return t.index(element)

# print(index_in_tuple((1, 2, 3), 2))
# # Count the occurrences of an element in a tuple.


# def count_in_tuple(t, element):
#     return t.count(element)

# print(count_in_tuple((1, 2, 2, 3), 2))
# Functions
# Define a function that returns the factorial of a number.

# factorial = 1
# for i in range(1, 6):
#     factorial *= i
# print(factorial)
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# print(factorial(5))
# # Define a function that returns the nth Fibonacci number.

# # bismillah
# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(5))
# # Define a function that checks if a number is prime.


# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# # print(is_prime(3))
# # print(is_prime(4))
# # print(is_prime(5))
# # print(is_prime(6))
# # print(is_prime(7))
# # print(is_prime(8))
# print(is_prime(1))
# print(is_prime(0))
# # bismillah
# def is_prime(n):
#     # if n <= 1:
#     #     return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# # print(is_prime(3))
# # print(is_prime(4))
# # print(is_prime(5))
# # print(is_prime(6))
# # print(is_prime(7))
# # print(is_prime(8))
# print(is_prime(1))
# print(is_prime(0))
# # bismillah
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return f"{n} is prime number"
# print(is_prime(3))
# print(is_prime(4))
# print(is_prime(5))
# print(is_prime(6))
# print(is_prime(7))
# print(is_prime(8))
# print(is_prime(1))
# print(is_prime(0))
# bismillah
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             print(f"{n} is not prim")
            
#         # else:
#         #     return True
#     print(f"{n} is prime")
# is_prime(3)
# is_prime(4)
# is_prime(5)
# is_prime(6)
# is_prime(7)
# is_prime(8)

# print(18%48)

# # Define a function that finds the greatest common divisor (GCD) of two numbers.
# a, b = 48, 18
# a, b = b, a % b
# print(a)
# print(b)
# print()
# a, b = 18, 12
# a, b = b, a % b
# print(a)
# print(b)
# print()
# a, b = 12, 6
# a, b = b, a % b
# print(a)
# print(b)
# print()

# a = 18
# b = 48
# print(a % b)
# def gcd(a=0, b=0):
#     while b:
#         a, b = b, a % b
#     print(a) 
#     print(b)

# gcd(48, 18)

# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     print(a) 

# gcd(90, 30)
# # bismillah
# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     print(a) 

# gcd(96, 30)
# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     print(a) 

# gcd(21,15 )
# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     print(a) 

# gcd(21, 30)
# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     print(a) 

# gcd(1, 10)
# Define a function that finds the least common multiple (LCM) of two numbers.







# Define a function that calculates the square of a number.

# bismillah
# def square(n):
#     return n ** 2

# print(square(4))
# Define a function that calculates the cube of a number.


# def cube(n):
#     return n ** 3

# print(cube(3))
# Define a function that returns the absolute value of a number.


# def absolute_value(n):
#     return abs(n)

# print(absolute_value(-5))
# # bismillah
# def absolute_value(n):
#     return abs(n)

# print(absolute_value(-17))
# Define a function that checks if a number is even.

# bismillah
# def is_even(n):
#     return n % 2 == 0

# print(is_even(4))
# print(is_even(14))
# print(is_even(40))
# print(is_even(46))
# print(is_even(47))
# print('bismillah')
# def is_even(n):
#     if    n % 2 == 0:
#         print("even :")
#     else:
#         print("odd :")

# is_even(2)
# is_even(4)
# is_even(8)
# is_even(6)
# is_even(7)
# print('bismillah')
# # Define a function that checks if a number is odd.


# # def is_odd(n):
# #     return n % 2 != 0

# # print(is_odd(3))
# def is_odd(n):
#     if n % 2 != 0:
#         print("odd :")
#     else:
#         print("even :")
# is_odd(1)
# is_odd(3)
# is_odd(5)
# is_odd(7)
# is_odd(8)
# Define a function that returns the maximum of three numbers.


# def max_of_three(a, b, c):
#     return max(a, b, c)

# print(max_of_three(1, 2, 3))
# Define a function that returns the minimum of three numbers.


# def min_of_three(a, b, c):
#     return min(a, b, c)

# print(min_of_three(1, 2, 3))
# Define a function that returns the sum of the digits of a number.


# def sum_of_digits(n):
#     return sum(int(digit) for digit in str(n))

# print(sum_of_digits(123))
# Define a function that returns the product of the digits of a number.
# Bismillah
def print_showNum(n):
    if n == 0:
        return
    print(n)
    print_showNum(n-1)
    print(n)

print_showNum(4)
# def product_of_digits(n):
#     product = 1
#     for digit in str(n):
#         product *= int(digit)
#     print(product) 
# product_of_digits(234)

# def product_of_digits(n):
#     product = 1
#     for digit in str(n):
#         product *= int(digit)
#     return product

# print(product_of_digits(123)
# bismillah
# Define a function that reverses the digits of a number.

# def reverse_digits(n):
#     print(int(str(n)[::-1]))

# reverse_digits(123)
# def reverse_digits(n):
#     return int(str(n)[::-1])

# print(reverse_digits(123))
# Bismillah
# Define a recursive function that returns the sum of all elements in a list.
# lst = [1, 2, 3]
# print(lst[0])
# print(lst[1])
# print(lst[2])
# print(lst[0:3])
# def sum_list(lst):
#     if not lst:
#         return 0
#     else:
#         return lst[0] + sum_list(lst[1:])

# sum_list([1, 2])

# def sum_list(lst):
#     if not lst:
#         return 0
#     else:
#         return lst[0] + sum_list(lst[1:])

# print(sum_list([1, 2, 3, 4, 5]))
# Define a recursive function that returns the product of all elements in a list.


# def product_list(lst):
#     if not lst:
#         return 1
#     else:
#         return lst[0] * product_list(lst[1:])

# print(product_list([1, 2, 3, 4, 5]))
# # Define a recursive function that returns the length of a list.


# def length_list(lst):
#     if not lst:
#         return 0
#     else:
#         return 1 + length_list(lst[1:])

# print(length_list([1, 2, 3, 4, 5]))
# Define a recursive function that finds the maximum element in a list.

# python
# Copy code
# def max_list(lst):
#     if len(lst) == 1:
#         return lst[0]
#     else:
#         return max(lst[0], max_list(lst[1:]))

# print(max_list([1, 2, 3, 4, 5]))
# Define a recursive function that finds the minimum element in a list.

# python
# Copy code
# def min_list(lst):
#     if len(lst) == 1:
#         return lst[0]
#     else:
#         return min(lst[0], min_list(lst[1:]))

# print(min_list([1, 2, 3, 4, 5]))
# File Handling
# Write a function to write a list of strings to a file.

# python
# Copy code
# def write_list_to_file(filename, lst):
#     with open(filename, 'w') as file:
#         for item in lst:
#             file.write(item + '\n')

# write_list_to_file('output.txt', ['hello', 'world'])
# Write a function to read all lines from a file into a list.

# python
# Copy code
# def read_file_to_list(filename):
#     with open(filename, 'r') as file:
#         return file.readlines()

# print(read_file_to_list('output.txt'))
# Write a function to append a string to a file.

# python
# Copy code
# def append_to_file(filename, string):
#     with open(filename, 'a') as file:
#         file.write(string + '\n')

# append_to_file('output.txt', 'append this line')
# Write a function to count the number of lines in a file.

# python
# Copy code
# def count_lines_in_file(filename):
#     with open(filename, 'r') as file:
#         return len(file.readlines())

# print(count_lines_in_file('output.txt'))
# Write a function to count the number of words in a file.

# python
# Copy code
# def count_words_in_file(filename):
#     with open(filename, 'r') as file:
#         return sum(len(line.split()) for line in file)

# print(count_words_in_file('output.txt'))
# Write a function to count the number of characters in a file.

# python
# Copy code
# def count_characters_in_file(filename):
#     with open(filename, 'r') as file:
#         return sum(len(line) for line in file)

# print(count_characters_in_file('output.txt'))
# List Comprehensions
# Generate a list of squares of numbers from 1 to 10.

# python
# Copy code
# squares = [x ** 2 for x in range(1, 11)]
# print(squares)
# Generate a list of even numbers from 1 to 20.

# python
# Copy code
# evens = [x for x in range(1, 21) if x % 2 == 0]
# print(evens)
# Generate a list of odd numbers from 1 to 20.

# python
# Copy code
# odds = [x for x in range(1, 21) if x % 2 != 0]
# print(odds)
# Generate a list of numbers divisible by both 3 and 5 from 1 to 100.

# python
# Copy code
# div_by_3_and_5 = [x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0]
# print(div_by_3_and_5)
# Generate a list of the first letters of each word in a given sentence.

# python
# Copy code
# sentence = "The quick brown fox jumps over the lazy dog"
# first_letters = [word[0] for word in sentence.split()]
# print(first_letters)
# Generate a list of the lengths of each word in a given sentence.

# python
# Copy code
# sentence = "The quick brown fox jumps over the lazy dog"
# word_lengths = [len(word) for word in sentence.split()]
# print(word_lengths)
# Lambda Functions
# Write a lambda function to add two numbers.

# python
# Copy code
# add = lambda a, b: a + b
# print(add(2, 3))
# Write a lambda function to find the maximum of two numbers.

# python
# Copy code
# maximum = lambda a, b: a if a > b else b
# print(maximum(2, 3))
# Write a lambda function to find the square of a number.

# python
# Copy code
# square = lambda x: x ** 2
# print(square(4))
# Write a lambda function to check if a number is even.

# python
# Copy code
# is_even = lambda x: x % 2 == 0
# print(is_even(4))
# Write a lambda function to check if a number is odd.

# python
# Copy code
# is_odd = lambda x: x % 2 != 0
# print(is_odd(3))
# Map, Filter, and Reduce
# Use map to square all numbers in a list.

# python
# Copy code
# numbers = [1, 2, 3, 4, 5]
# squares = list(map(lambda x: x ** 2, numbers))
# print(squares)
# Use filter to get all even numbers in a list.

# python
# Copy code
# numbers = [1, 2, 3, 4, 5]
# evens = list(filter(lambda x: x % 2 == 0, numbers))
# print(evens)
# Use reduce to calculate the product of all numbers in a list.

# python
# Copy code
# from functools import reduce

# numbers = [1, 2, 3, 4, 5]
# more
# ChatGPT
# Map, Filter, and Reduce (continued)
# Use reduce to calculate the product of all numbers in a list.

# python
# Copy code
# from functools import reduce

# numbers = [1, 2, 3, 4, 5]
# product = reduce(lambda x, y: x * y, numbers)
# print(product)
# Use map to convert all strings in a list to uppercase.

# python
# Copy code
# strings = ["hello", "world"]
# uppercased = list(map(lambda s: s.upper(), strings))
# print(uppercased)
# Use filter to get all words starting with 'a' in a list.

# python
# Copy code
# words = ["apple", "banana", "avocado"]
# a_words = list(filter(lambda word: word.startswith('a'), words))
# print(a_words)
# Use reduce to find the longest word in a list.

# python
# Copy code
# from functools import reduce

# words = ["apple", "banana", "avocado"]
# longest_word = reduce(lambda a, b: a if len(a) > len(b) else b, words)
# print(longest_word)
# Classes and Objects
# Define a class representing a Person with attributes name and age.

# python
# Copy code
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"Person(name={self.name}, age={self.age})"

# person = Person("John", 30)
# print(person)
# Add a method greet to the Person class that prints a greeting message.

# python
# Copy code
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# person = Person("John", 30)
# person.greet()
# Define a class representing a Circle with attributes radius and a method area that returns the area of the circle.

# python
# Copy code
# import math

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius ** 2

# circle = Circle(5)
# print(circle.area())
# Define a class representing a Rectangle with attributes width and height, and a method area that returns the area of the rectangle.

# python
# Copy code
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

# rectangle = Rectangle(4, 5)
# print(rectangle.area())
# Define a class representing a Square that inherits from Rectangle.

# python
# Copy code
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

# class Square(Rectangle):
#     def __init__(self, side_length):
#         super().__init__(side_length, side_length)

# square = Square(4)
# print(square.area())
# Define a class representing a BankAccount with attributes balance and methods deposit and withdraw.

# python
# Copy code
# class BankAccount:
#     def __init__(self):
#         self.balance = 0

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#         else:
#             print("Insufficient funds")

#     def __str__(self):
#         return f"BankAccount(balance={self.balance})"

# account = BankAccount()
# account.deposit(100)
# account.withdraw(50)
# print(account)
# Inheritance and Polymorphism
# Define a class Animal with a method make_sound and subclasses Dog and Cat that override make_sound.

# python
# Copy code
# class Animal:
#     def make_sound(self):
#         pass

# class Dog(Animal):
#     def make_sound(self):
#         return "Woof!"

# class Cat(Animal):
#     def make_sound(self):
#         return "Meow!"

# dog = Dog()
# cat = Cat()
# print(dog.make_sound())
# print(cat.make_sound())
# Define a class Vehicle with a method start and subclasses Car and Bike that override start.

# python
# Copy code
# class Vehicle:
#     def start(self):
#         pass

# class Car(Vehicle):
#     def start(self):
#         return "Car starting..."

# class Bike(Vehicle):
#     def start(self):
#         return "Bike starting..."

# car = Car()
# bike = Bike()
# print(car.start())
# print(bike.start())
# Define a class Shape with a method area and subclasses Triangle and Circle that override area.

# python
# Copy code
# import math

# class Shape:
#     def area(self):
#         pass

# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def area(self):
#         return 0.5 * self.base * self.height

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius ** 2

# triangle = Triangle(3, 4)
# circle = Circle(5)
# print(triangle.area())
# print(circle.area())
# Define a class Employee with a method get_salary and subclasses Manager and Developer that override get_salary.

# python
# Copy code
# class Employee:
#     def get_salary(self):
#         pass

# class Manager(Employee):
#     def get_salary(self):
#         return "Manager salary is $5000"

# class Developer(Employee):
#     def get_salary(self):
#         return "Developer salary is $4000"

# manager = Manager()
# developer = Developer()
# print(manager.get_salary())
# print(developer.get_salary())
# Error Handling
# Write a function that divides two numbers and handles division by zero using try-except.

# python
# Copy code
# def divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return "Cannot divide by zero"

# print(divide(10, 2))
# print(divide(10, 0))
# Write a function that converts a string to an integer and handles invalid input using try-except.

# python
# Copy code
# def string_to_int(s):
#     try:
#         return int(s)
#     except ValueError:
#         return "Invalid input"

# print(string_to_int("123"))
# print(string_to_int("abc"))
# File Handling (continued)
# Write a function to copy the contents of one file to another.

# python
# Copy code
# def copy_file(source, destination):
#     with open(source, 'r') as src:
#         with open(destination, 'w') as dst:
#             dst.write(src.read())

# copy_file('source.txt', 'destination.txt')
# Write a function to count the number of occurrences of a word in a file.

# python
# Copy code
# def count_word_in_file(filename, word):
#     with open(filename, 'r') as file:
#         return file.read().count(word)

# print(count_word_in_file('output.txt', 'line'))
# Random Module
# Generate a random number between 1 and 100.

# python
# Copy code
# import random

# random_number = random.randint(1, 100)
# print(random_number)
# Generate a random float number between 0 and 1.

# python
# Copy code
# import random

# random_float = random.random()
# print(random_float)
# Shuffle a list of numbers.

# python
# Copy code
# import random

# numbers = [1, 2, 3, 4, 5]
# random.shuffle(numbers)
# print(numbers)
# Sorting and Searching
# Sort a list of numbers in ascending order.

# python
# Copy code
# numbers = [5, 3, 8, 1, 2]
# numbers.sort()
# print(numbers)
# Sort a list of numbers in descending order.

# python
# Copy code
# numbers = [5, 3, 8, 1, 2]
# numbers.sort(reverse=True)
# print(numbers)
# Use sorted to sort a list of tuples by the second element.

# python
# Copy code
# tuples = [(1, 'one'), (2, 'two'), (3, 'three')]
# sorted_tuples = sorted(tuples, key=lambda x: x[1])
# print(sorted_tuples)