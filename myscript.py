# 1.Indentation is very important in python
# 2.


# name = input('What is your name? ') #inPut
# print('Hi! ' + name) #output
# print("Hi!", name)
# print(f'Hi! {name} welocome') #Formatted string literals
# print(f"Hi! {name.upper()}")
# print('Very nice to meet you,{}!'.format(name)) #str.format()
# print("Hi {} is my name".format(name))

# ==================functions============
#
# def greet_someone():
#     name = input("What is you name? ")
#     hometown = input('And where are you from? ')
#     print('Very nice to meet you, {}!'.format(name), f'from {hometown}')

# greet_someone()
#
#

# ============variables and if Statements==============
#
# name = "Grace"
# res = input('Is {} your real name'.format(name))
# if res.lower() == "yes":
#     print('Her real name is {}'.format(name))
# else:
#     print("It's not her real name" * 10)
#
#

# printing the Data type
#
# tem = str(97.0)
# num = 2
# print(type(num))
#
#

# int
#
# tem = int(101.2)
# print(tem) # prints 101
#
#

# Float
#
# tem = float(101.3022)
# print(tem)
#
#

# Boolean
#
# raining = True
# raining = bool("True") #Returns true all the time unless is empty
# print(raining)
#
#

# OPerators
#
# a = 2
# b = 8
# print("Exponential",a**2) #Exponential
# print("Addition",a + b) #Addition
# print("Division",b / a) #Division
# print("Floor Division",b // a) #Division
# print("Substraction",b - a) #Substraction
# print("Modulus",b % a) #Modulus
#
#

# Assignment operators
#

#
#

# Comparison operators
#

#
#

# Logical operators
#
# print(2 == 2 and 1 == 1)
#
#

# if, elif and else statement
# #
# score = 90
# if score >= 80:
#     print('You pass the course!')
#
#

# Loops
#

# == list ==
# nums = [1,2,3,4,5]
# for item in nums:
#     print(item + 1)

# == range ==
# for i in range(3):
#     print(i)

# == nested for loops ==
# teams = [['Jody', 'Abe'], ['Abhishek', 'Kim'], ['Taylor', 'Jen']]
# for team in teams:
#     for name in team:
#         print(name)
#
#

# Pass, Break, Continue
#
# names = ['Joyce', 'Hannah', 'Manny', 'Manoj', 'Ezekiel']

# == Pass ==
# for name in names:
#     if "j" in name.lower():
#         pass
#     else:
#         print(name)

# == break ==
# for name in names:
#     if "h" in name.lower():
#         break
#     else:
#         print(name)

# == continue ==
# for name in names:
#     if "h" in name.lower():
#         continue
#     else:
#         print(name)
#
#

# Error handler
#
# nums = [0,1,2,3,]

# try:
#     print(sum(nums))
# except:
#     print('Connot print the Sum! Your variables are not numbers.')
# finally:
#     print('Hope you got the results you want!')
#
#

# def add_three(num1, num2, num3):
#     sum_three = num1 + num2 + num3
#     return sum_three

# sum_output = add_three(2,4,6)

# print(sum_output)

# def greetings(language):
#     if language == "Spanish":
#         greeting = "Hola"

#     elif language == "English":
#         greeting = "Hello"

#     elif language == "French":
#         greeting = "Bonjour"

#     print(greeting)

# greetings("French")

#
#

# recursion
#
# def factorial(num):
#     if num == 1:
#         return 1
#     else:
#         return num * factorial(num-1)

# print(factorial(3))


# def factorial(num):
#    call_stack = []
#    if num == 1:
#        print('base case reached! Num is 1.')
#        return 1
#    else:
#        call_stack.append({'input': num})
#        print('call stack: ', call_stack)
#        return num * factorial(num-1)

# factorial(5)

#
#

# lambda
#
# sum_num = lambda x: x + 2
# print(sum_num(2))
# print(sum_num(5))
#
#


# Classes and Objects
#
# class Dog:
#     # this is a blank class
#     pass

# pepper = Dog()
# print(Dog())
#
#


#
#
# class ClassSchedule:
#     def __init__(self, course):
#         self.course = course

#     def __del__(self):
#         print('You successfully deleted your schedule')

# course_name = input("What is the course name: ")
# first = ClassSchedule(course_name)
# # print("The course is",first.course)
# del first
#
#

# Public Access Modifier
#
# class ClassSchedule:
#     def __init__(self, name, course, time):
#         self.course = course
#         self.name = name
#         self.time = time

#     def display_course(self):
#         print(f'Course: {self.course}, Time: {self.time}, Name: {self.name}')

# name = input("Enter your name: ")
# course = input("Enter the course: ")
# time = input("Enter the time: ")

# sched = ClassSchedule(name, course, time)

# # sched.display_course()
# # print(sched.course)
#
#

# Protect Access Modifier
#
# class ClassSchedule:
#     def __init__(self, course, time):
#         self._course = course
#         self._time = time

#     def display_course(self):
#         print(f'Course: {self._course}, Time: {self._time}')

# sched = ClassSchedule("Biology", "9:00")
# sched.display_course()
#   
#

#Private Access Modifier
#
# class ClassSchedule:
#     def __init__(self, course, time):
#         self.__course = course
#         self.__time = time

#     def display_course(self):
#         print(f'Course: {self.__course}, Time: {self.__time}')

# sched = ClassSchedule('English', "9:00")
# sched.display_course() #This renders
# print(sched.__course) #throws an error
#
#