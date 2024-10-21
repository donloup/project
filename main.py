# #Boolean
# is_student = True
# for_sale = False
# is_online = False
# if is_student:
#     print("You are a student")
# else:
#     print("You are NOT a student")
# if for_sale:
#     print("That item is for sale")
#
# else:
#     print("That item is NOT available")
#
# if is_online:
#     print("You are online")
# else:
#     print("You are NOT online")
#
# # Typecasting = converting a variable from one data type to another
# #     str(), int(), float(), bool()
#
# name = "Bron Code"
# age = 24
# gpa = 3.4
# is_student = True
#
# print(type(gpa))
#
# gpa = int(gpa)
# print(gpa)
#
# name = bool(name)
# print(name)
#
# #input() = function that prompts the user to enter data
# #  Returns the entered data as a string
#
# name = input("What is your name?:")
# age = input("How old are you?:")
#
# age = int(age)
# age = age + 1
# print(f"Hello {name}!")
# print("Happy Birthday")
# print(f"You are {age} years old")
#
#
# # Exercise 1 Rectangle Area Calc
#
# length = float(input("Enter the length:"))
# width = float(input("Enter the width:"))
#
# area = length * width
#
# print(area)
#
# #Exercise 2 shopping Cart Program
#
# item = input("What item would you like to buy?:")
# price = float(input("What is the price?:"))
# quantity = int(input("How many would you like?:"))
# total = price * quantity
#
# print(f"You have bought {quantity} x {item}/s")
# print(f"You total is ${total}")
#
#
# # madlibs game
# # word game where you create a story
# # by filling in blanks with random words
#
# adjective1 = input("Enter an adjective (description):")
# noun1 = input("Enter a noun (person, place, thing:")
# adjective2 = input("Enter an adjective (description):")
# verb1 = input("Enter a verb ending with 'ing'")
# adjective3 = input("Enter an adjective (description):")


#
# print(f"Today I went to a {adjective1} zoo.")
# print(f"In a exhibit, I saw a {noun1}")
# print(f"{noun1} was {adjective2} and {verb1}")
# print(f"I was {adjective3}!")

#
# friends = 10
# friends = friends + 1
# friends = friends - 2
# friends -= 2
# friends += 1
# friends = friends * 3
# friends = friends / 2
# friends /= 2
# friends = friends ** 2

# reminder = friends % 2
#
# print(friends)

# x = 3.14
# y = 4
# z = 5
# #result = round(x)
# #result =abs(y)
# #result = pow(5,3)
# #result = max(x,y,z)
# result = min(x,y,z)
# print(result)

import math

# x = 9.9

# print(math.pi)
# print(math.e)
#result = math.sqrt(x)
#result = math.ceil(x)
# result = math.floor(x)
# print(result)


# radius = float(input('Enter the radius of a circle:'))
#
#
# circumference = 2 * math.pi * radius
# print(f"The circumference is: {round(circumference, 2)}cm")

# radius = float(input('Enter the radius of a circle:'))
# area =math.pi * pow(radius, 2)
#
# print(f"The area of the circle is: {round(area, 2)}cm^2")

# a = float(input("Enter side A:"))
# b = float(input("Enter side B:"))
#
# c = math.sqrt(pow(a,2) + pow(b,2))
#
# print(f"Side C = {c}")

# if = do some code only IF some condition is True
#       Else do something else

# age = int(input("Enter your age:"))
#
# if age >= 100:
#     print("You are too old to sign up!")
# elif age >= 18:
#     print("You are now signed up!")
# elif age < 0:
#     print("You haven't born yet!")
# else:
#     print("You must be 18+ to sign up")


# name = input("Enter your name:")
#
# if name == "":
#     print("You did not type in your name!")
# else:
#     print(f"Hello {name}")

# Python calculator
# operator = input("Enter an operator (+ - * /): ")
# num1 = float(input("Enter the 1st number: "))
# num2 = float(input("Enter the 2nd number: "))
#
# if operator == "+":
#     result = num1 + num2
#     print(round(result, 3))
# elif operator == "-":
#     result = num1 - num2
#     print(round(result, 3))
# elif operator == "*":
#     result = num1 * num2
#     print(round(result, 3))
# elif operator == "/":
#     result = num1 / num2
#     print(round(result, 3))
# else:
#     print(f"{operator} is not a valid operator")

# python weight converter

# weight = float(input("Enter your weight: "))
# unit = input("Kilograms or Pounds? (K or L): ")
#
# if unit == "K":
#     weight = weight * 2.205
#     unit = "Lbs."
#     print(f"Your weight is: {round(weight, 1)} {unit}")
# elif unit == "L":
#     weight = weight / 2.205
#     unit = "kgs."
#     print(f"Your weight is: {round(weight, 1)} {unit}")
# else:
#     print(f"{unit} was not valid")
#
# print(f"Your weight is: {round(weight, 1)} {unit}")

# unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
# temp = float(input("Enter the temperature: "))
#
# if unit == "C":
#     temp = round((9 * temp) / 5 + 32, 1)
#     print(f"The temperature in Fahrenheit is: {temp}F")
# elif unit == "F":
#     temp = round((temp - 32) + 5 / 9, 1)
#     print(f"The temperature in Celsius is: {temp}C")
# else:
#     print(f"{unit} is invalid unit of measurement")

# temp = 57
# ia_raining = True
#
# if temp > 35 or temp < 0 or ia_raining:
#     print("The outdoor event is cancelled")
# else:
#     print("The outdoor event is still scheduled")

# conditional expression = a one-line shortcut for the if-else statement(Ternary operator)
#                          print or assign one of two values based on a condition
#                          X if condition else Y

# num = 5
# a = 6
# b = 7
#
# age = 25
# temperature = 19
# user_role = "guest"
# print ("Positive" if num > 0 else "Negative")
# result = "EVEN" if num % 2 == 0 else "ODD"
# max_num = a if a > b else b
# min_num = a if a < b else b
# status = "Adult" if age >= 18 else "child"
# weather = "HOT" if temperature > 20 else "COLD"
# access_level = "Full Access" if user_role == "admin" else "Limited Access"
#
# print(access_level)

# name = input("Enter your full name: ")

# result = len(name)
# result = name.find("e")
# result = name.rfind("o")
# name = name.capitalize()
# name = name.upper()
# name = name.lower()
# result = name.isdigit()
# result = name.isalpha()

# print(result)

# print(help(str))

# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

#
# username = input("Enter a username: ")
#
#
#
# if len(username) > 12:
#     print("Your username can't be more than 12 characters")
# elif not username.find(" ") == -1:
#     print("Your username can't contain spaces")
# elif not username.isalpha():
#     print("Your username can't contain numbers")
# else:
#     print(f"welcome {username}")


# Indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end : step]

# credit_number = "1234-5678-9012-3456"

# print(credit_number[0])
# print(credit_number[:4])
# print(credit_number[5:9])
# print(credit_number[10:14])
# print(credit_number[5:])
# print(credit_number[-1])
# print(credit_number[::3])

# last_digits = credit_number[-4:]
# print(f"xxxx-xxxx-xxxx-{last_digits}")

# credit_number = credit_number[::-1]
# print(credit_number)

# format specifiers = {value: flags} format a value based on what
#                              flags are inserted

# price1 = 3.14159
# price2 = -957.654566774
# price3 = 12.4367458
#
# print(f"Price 1 is ${price1:010}")
# print(f"Price 2 is ${price2:<10}")
# print(f"Price 3 is ${price3:>2f}")
# print(f"Price 3 is ${price3: }")


# While loop = execute some code when some condition remain true

# name = input("Enter your name: ")
#
# while name == "":
#     print("You did not enter your name")
#     name = input("Enter your name: ")
# print(f"Hello {name}")


# age = int(input("Enter your age: "))
#
# while age < 0:
#     print("Age can't be negative")
#     age = int(input("Enter your age: "))
#
# print(f"You are {age} years old")


# food = input("Enter a food you like (q to quit): ")
#
# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter a food you like (q to quit): ")
#
# print("bye")



# num = int(input("Enter a # between 1 - 10:"))
#
# while num < 1 or num > 10:
#     print(f"{num} is not valid")
#     num = print(input("Enter a # between 1 - 10: "))
#
# print(f"Your number is {num}")


# python compound interest calculator

# principle = 0
# rate = 0
# time = 0
#
# while True:
#     principle = float(input("Enter the principe amount: "))
#     if principle < 0:
#         print("principle can't be less than zero")
#     else:
#         break
#
#
# while True:
#     rate = float(input("Enter the interest rate: "))
#     if rate < 0:
#         print("interest rate can't be less than zero")
#     else:
#         break
#
# while True:
#     time = int(input("Enter the time in years: "))
#     if time < 0:
#         print("time can't be less than zero")
#     else:
#         break
#
# total = principle * pow((1 + rate / 100), time)
# print(f"Balance after {time} years/s: ${total:.2f}")

# print(principle)
# print(rate)
# print(time)


# for loops = execute a block of code a fixed number of times
#           You can iterate over a range, string, sequence, etc.

# for x in range(1, 11, 3):
#     print(x)

# for x in reversed(range(1, 11)):
#     print(x)
#
# print("Happy New year!")

# credit_card = "1234-5678-9012-3456"
#
# for x in credit_card:
#     print(x)

# for x in range(1, 21):
#     if x == 13:
#         continue
#     else:
#         print(x)


# for x in range(1, 21):
#     if x == 13:
#         break
#     else:
#         print(x)

# import time
#
# my_time = int(input("Enter the time in seconds: "))
#
# # for x in range(0, my_time):
# for x in range(my_time, 0, -1):
#     seconds = x % 60
#     minutes = int(x / 60) % 60
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#
#
#     time.sleep(1)
#
# print("TIME'S UP!")

# nested loop = A loop within another loop (outer, inner)
#             outer loop:
#                  inner loop:

# for x in range(3):
#
#     for y in range(1, 10):
#     # print(x)
#          print(y, end= " ")
#     print()

# rows = int(input("Enter the # of rows: "))
# columns = int(input("Enter the # of column: "))
# symbol = input("Enter a symbol to use: ")
#
# for x in range(rows):
#     for y in range(columns):
#
#          print(symbol, end=" ")
#     print()


# collection = single "variable" used to store mutiple value
#   List  = [] ordered and changeable. Duplicates OK
#   Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ["apple", "orange", "banana", "coconut"]
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print(fruits[0])
print("pineapple" in fruits)

fruits[0] = "pineapple"
fruits.append("mangoes")
fruits.remove("apple")


for fruit in fruits:
    print(fruit)


