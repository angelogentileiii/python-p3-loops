#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i in range(10, 0, -1):
        print(i)
        i -= 1
    
    print("Happy New Year!")

def square_integers(int_list):
    return [num ** 2 for num in int_list]

def fizzbuzz():
    for x in range (1, 101):
        if not x % 15:
            print("FizzBuzz")
        elif not x % 5:
            print("Buzz")
        elif not x % 3:
            print("Fizz")
        else:
            print(x)
