#!/usr/bin/env python3

def admin_login(username, password):
    if ((username == 'admin') or (
        username == 'ADMIN')) and (
        password == '12345'):
        return 'Access granted'
    else:
        return 'Access denied'

def hows_the_weather(temperature):
    if temperature > 85:
        return "It's too dang hot out there!"
    elif temperature <= 65 and temperature >= 40:
        return "It's a little chilly out there!"
    elif temperature < 40:
        return "It's brisk out there!"
    else:
        return "It's perfect out there!"

def fizzbuzz(num):
    if (num % 3 == 0) and (num % 5 == 0):
        return 'FizzBuzz'
    elif num % 5 == 0:
        return 'Buzz'
    elif num % 3 == 0:
        return 'Fizz'
    else:
        return num

def calculator(operation, num1, num2):
    if (isinstance(num1, int) or isinstance(num1, float)) and (
        isinstance(num2, int) or isinstance(num2, float)):
        if operation == '+':
            return num1 + num2
        if operation == '-':
            return num1 - num2
        if operation == '*':
            return num1 * num2
        if operation == '/':
            return num1 / num2
        else:
            print('Invalid operation!')
            return None
    else:
        return "Those number aren't numbering!"
