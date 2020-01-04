#Even Fibonacci numbers
#Day: 1
#Author: Dawid Ciechowski
#Language: Python

def problem2():
    num1, num2 = 1, 1
    sum = 0
    while num2 < 4000000:
        if num2 % 2 == 0:
            sum += num2
        num1, num2 = num2, num1+num2

    return sum

print(problem2())