# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)

# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default),
# and stops before a specified number.
# Syntax: range(start, stop, step)
# start- Optional. An integer number specifying at which position to start. Default is 0
# stop- Required. An integer number specifying at which position to stop (not included)
# step- Optional. An integer number specifying the incrementation. Default is 1


#2. Using range() with Step Values:
# for i in range(2, 20, 3):
#     print (i)

#Lab 4: Using continue in Loops
#1. Skipping even numbers, how to use the continue statement to skip the current iteration of a loop and move on to the next one.

# for i in range(20):
#     if i % 2 == 0:
#         continue
#     print(i)

#############################
#Exercise 1:Problem: Write a program that uses a while loop to print all even numbers from 2 to 20.

# def print_even_numbers():
#     number = 2
#     while number <= 20:
#         print(number)
#         number += 2
# print_even_numbers()
#################################
#2. Create a program that counts down from 10 to 1 and prints each number.
# def countdown():
#     number = 10
#     while number > 0:
#         print(number)
#         number -= 1
# countdown()

############################################
#. Implement a while loop that sums numbers from 1 to 100 and prints the total.
# def sum_numbers():
#     total = 0
#     number = 1
#     while number<= 100:
#         total += number
#         number += 1
#     print ("Total sum:", total)
# #sum_numbers()

# number = 1
# total = 0
# for number in range(1, 101):
#     total += number
# print("Total sum:", total)

############################################
#Lab 2:Write a program that prints each character of a string on a new line using a for loop

# def print_characters(s):
#     for char in s:
#         print(char)
#
# # Example usage
# print_characters("Hello")
###########################################
import math
#Exercise 3:Problem: Implement a for loop to calculate and print the factorial of a number.
# def factorial(n):
#     result = 1
#     for i in range(1, n+1):
#         result *= i
#         print("Factorial:", result)
# factorial(5)
###########################
# def greet_names(names):
#     for name in names:
#         print(f"Hello, {name}!")
#
# # Example usage
# greet_names(["Alice", "Bob", "Charlie"])

#####################################################
# def print_numbers():
#     for number in range(5, 16):
#         print (number)
#     print_numbers()


#######################################################
#Lab 3:  range() to print numbers from 5 to 15.
# def print_numbers():
#     for number in range(5, 16):  # range(5, 16) includes numbers from 5 to 15
#         print(number)
#
# # Example usage
# print_numbers()
#################################################################
#Exercise 2:prints the squares of numbers from 1 to 10 using range().
# def print_squares():
#     for number in range(1, 11):  # range(1, 11) includes numbers from 1 to 10
#         print(number ** 2)
#
# # Example usage
# print_squares()

###############################################
#Exercise 3:Problem: Implement a for loop with range() to generate a list of even numbers from 0 to 20.

# def generate_even_numbers():
#     even_numbers = [number for number in range(0, 21, 2)]  # range(0, 21, 2) generates even numbers from 0 to 20
#     print(even_numbers)
#
# # Example usage
# generate_even_numbers()
############################################################
#Lab 4:skips all the numbers divisible by 3 and prints the rest from 1 to 15.
# def print_non_divisible_by_3():
#     for number in range(1, 16):  # Loop from 1 to 15
#         if number % 3 == 0:
#             continue  # Skip numbers divisible by 3
#         print(number)
#
# # Example usage
# print_non_divisible_by_3()

#####################################################
#Exercise 2: Create a program that iterates over a list of numbers and prints only those that are greater than 5, skipping numbers less than or equal to 5.
# def print_numbers_greater_than_5(numbers):
#     for number in numbers:
#         if number <= 5:
#             continue  # Skip numbers less than or equal to 5
#         print(number)
#
# # Example usage
# print_numbers_greater_than_5([1, 3, 5, 7, 9, 11])

##or###ORRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR

# numbers = [1, 3, 5, 7, 9, 11]
# for number in numbers:
#     if number <= 5:
#         continue  # Skip numbers less than or equal to 5
# print(number)
#####################################################################
#Exercise 3:Problem: Implement a for loop that prints numbers from 1 to 10, but skips printing the number 7.

# def print_numbers_excluding_7():
#     for number in range(1, 11):  # Loop from 1 to 10
#         if number == 7:
#             continue  # Skip the number 7
#         print(number)
#
# # Example usage
# print_numbers_excluding_7()
########################or#########################or
# for number in range(1, 11):  # Loop from 1 to 10
#     if number == 7:
#         continue  # Skip the number 7
#     print(number)

#####################################################################
#Lab 5:Write a program that finds the first number in a list that is greater than 50 and stops iterating when it finds it
# def find_first_greater_than_50(numbers):
#     for number in numbers:
#         if number > 50:
#             print(f"First number greater than 50: {number}")
#             break  # Exit the loop once the condition is met
#
# # Example usage
# find_first_greater_than_50([10, 25, 30, 55, 60, 75])

#############################ORRRRRRRRRRRRRRRRRRRRRRRRRRRRRR##################ORRRRRRRRRRRRRRRRRRR
# numbers = [10, 25, 30, 55, 60, 75]
# for number in numbers:
#     if number > 50:
#         print(f"First number greater than 50: {number}")
#         break  # Exit the loop once the condition is met

#######################################################################

#Exercise 2:Problem: Create a program that uses a while loop to ask for user input until the user enters the word "stop".
# def ask_until_stop():
#     while True:
#         user_input = input("Enter something (type 'stop' to exit): ")
#         if user_input.lower() == 'stop':
#             break  # Exit the loop if the user types 'stop'
#
# # Example usage
# ask_until_stop()
####################################################################################
#Exercise 3:Problem: Implement a for loop that iterates through numbers from 1 to 20, but breaks the loop when it encounters a number divisible by 5.
# for number in range(1, 21):  # Loop from 1 to 20
#     if number % 5 == 0:
#         print(f"Number divisible by 5 found: {number}")
#         break  # Exit the loop once a number divisible by 5 is encountered

        ################################ORRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
# def print_until_divisible_by_5():
#     for number in range(1, 21):  # Loop from 1 to 20
#         if number % 5 == 0:
#             print(f"Number divisible by 5 found: {number}")
#             break  # Exit the loop once a number divisible by 5 is encountered
#
# # Example usage
# print_until_divisible_by_5()

#############################################################################################################

#Lab 6:Problem: Write a program that prints each item in a list of fruits in uppercase.
# def print_fruits_uppercase(fruits):
#     for fruit in fruits:
#         print(fruit.upper())  # Convert each fruit to uppercase and print
#
# # Example usage
# print_fruits_uppercase(['apple', 'banana', 'cherry'])

########################################################################################################
# Exercise 2:
# Problem: Create a program that iterates over a list of numbers and prints the sum of all the numbers.
# def sum_of_numbers(numbers):
#     total_sum = 0
#     for number in numbers:
#         total_sum += number  # Add each number to the total sum
#     print(f"Sum of all numbers: {total_sum}")
#
# # Example usage
# sum_of_numbers([1, 2, 3, 4, 5])
#########################################################################################
# Exercise 3:
# Problem: Implement a for loop to create a new list containing only the odd numbers from an existing list.
#
# Solution:
#
# def filter_odd_numbers(numbers):
#     odd_numbers = []
#     for number in numbers:
#         if number % 2 != 0:
#             odd_numbers.append(number)  # Add odd numbers to the new list
#     return odd_numbers
#
# # Example usage
# odd_numbers = filter_odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(f"Odd numbers: {odd_numbers}")

###########################################################################################

#Lab:7: Iterating Over Dictionaries.  prints all the keys in a dictionary of student names and grades.
# def print_student_keys(student_grades):
#     for key in student_grades:
#         print(key)  # Print each key in the dictionary
#
# # Example usage
# print_student_keys({'Alice': 85, 'Bob': 90, 'Charlie': 78})

##########ORRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
# student_grades = {'Alice': 85, 'Bob': 90, 'Charlie': 78}
# for key in student_grades:
#     print(key)

###############################################################################
#2. Create a program that iterates over a dictionary and prints the average value of all the numeric values.
# def average_of_values(data):
#     total_sum = 0
#     count = 0
#     for value in data.values():
#         total_sum += value  # Sum all the values
#         count += 1
#     if count > 0:
#         average = total_sum / count
#         print(f"Average value: {average}")
#     else:
#         print("No values to average")
#
# # Example usage
# average_of_values({'Alice': 85, 'Bob': 90, 'Charlie': 78})
####################ORRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
# data= {'Alice': 85, 'Bob': 90, 'Charlie': 78}
# total_sum = 0
# count = 0
# for value in data.values():
#     total_sum += value  # Sum all the values
#     count += 1
# if count > 0:
#     average = total_sum / count
#     print(f"Average value: {average}")
# else:
#     print("No values to average")

##############################################################
#Exercise 3:Problem: Implement a program that prints the keys and values of a dictionary in a formatted string
# def print_dict_items(data):
#     for key, value in data.items():
#         print(f"Key: {key}, Value: {value}")  # Print key-value pairs
#
# # Example usage
# print_dict_items({'Alice': 85, 'Bob': 90, 'Charlie': 78})
#############################################################################################
# Lab 8: Handling None in Loops
# Exercise 1:
# Problem: Write a program that replaces None values in a list with the string "Unknown" and prints the modified list.
# def replace_none_with_unknown(data_list):
#     modified_list = ['Unknown' if item is None else item for item in data_list]
#     print(modified_list)
#
# # Example usage
# replace_none_with_unknown(['Alice', None, 'Bob', None, 'Charlie'])
# Exercise 2:
# Problem: Create a program that filters out None values from a list and prints the remaining values.
#
# Solution:
# def filter_none_values(data_list):
#     filtered_list = [item for item in data_list if item is not None]
#     print(filtered_list)
#
# # Example usage
# filter_none_values(['Alice', None, 'Bob', None, 'Charlie'])

###################################################################################################
#Exercise 3:Problem: Implement a for loop to check if any value in a dictionary is None and print a message if so.

# def check_none_in_dict(data_dict):
#     for key, value in data_dict.items():
#         if value is None:
#             print(f"Value for key '{key}' is None.")
#
# # Example usage
# check_none_in_dict({'Alice': 85, 'Bob': None, 'Charlie': 78})
####################################################################################
#Exception
#Lab 1: Handling SyntaxError
# def greet():
#     print("Hello!")

#Lab 2: Handling ValueError
# Description:
# Explore ValueError, which occurs when a function receives an argument of the correct type but inappropriate value. You'll practice handling such errors using try and except.
# try:
#     num = int("abc")
# except ValueError:
#     print("Cannot convert to an integer.")
    #######################

# try:
#     age = int(input("Enter your age: "))
# except ValueError:
#     print("Please enter a valid number.")

############################################################
#Lab3: In this lab, you'll learn how to use try and except blocks to catch and handle exceptions, preventing your program from crashing.

# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Cannot divide by zero.")

##########################################################
# try:
#     num = int("cat")
#     result = num / 0
# except ValueError:
#     print("Invalid number.")
# except ZeroDivisionError:
#     print("Cannot divide by zero.")

###########################################################
#Lab 4: Handling NameError:Learn to handle NameError, which occurs when a local or global name is not found. This lab focuses on identifying the cause and resolving NameError.
#1. Using Undefined Variables:

# try:
#     print(x)
# except NameError:
#     print("Variable 'x' is not defined.")
#orrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr
# x = 10
# print(x)  # This will now work correctly.

###########################################################################
#Lab 5: Using else with try: Explore the use of else in try and except blocks. The else block runs when no exception occurs, allowing you to separate the normal execution flow from error handling.
# try:
#     num = int("100")
# except ValueError:
#     print("Invalid number.")
# else:
#     print("Conversion successful:", num)
##############################################################################
#Using else to Proceed After Successful Operation:
# try:
#     with open("sample.txt", "r") as file:
#         content = file.read()
# except FileNotFoundError:
#     print("File not found.")
# else:
#     print("File content:", content)

################################################################################
#Lab 6: Using pass in Exception Handling:Learn how to use pass in an except block to ignore certain exceptions. This is useful when you want to handle an exception without taking any specific action.
# try:
#     num = int("abc")
# except ValueError:
#     pass  # Do nothing if a ValueError occurs.
##############################################################
# try:
#     num = int(input("Enter a number: "))
# except ValueError:
#     print("That was not a number.")
# except:
#     pass  # Ignore any other exceptions.
################################################################################
#Lab 7: Raising Exceptions with raise,This lab focuses on using raise to manually trigger exceptions. You'll learn how to raise exceptions when certain conditions in your code are not met.
#1.Raising a ValueError:
# x = -5
#
# if x < 0:
#     raise ValueError("Negative value encountered.")
###############################################################
#Raising a Custom Exception:
# class NegativeNumberError(Exception):
#     pass
#
# num = -10
# if num < 0:
#     raise NegativeNumberError("Negative numbers are not allowed.")