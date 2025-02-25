# Description: This is a program that has a loop that executes 100 times. Numbers that are divisible by 5 are replaced with "Fizz", numbers that are divisible by 8 are replaced with "Bizz", and numbers that are divisible by both 5 and 8 are replaced with "FizzBizz".
# Author: Landon - Group 6
# Date: Feb 17, 2025 - Feb 26, 2025

for a in range(1, 101):
    if a % 5 == 0 and a % 8 == 0:
        print("FizzBizz")
    elif a % 5 == 0:
        print("Fizz")
    elif a % 8 == 0:
        print("Bizz")
    else:
        print(a)