#Multiples of 3 and 5 
#Day: 1
#Author: Dawid Ciechowski
#Language: Python

def problem1():
    return sum([x for x in range(1,1000) if x % 3 == 0 or x % 5 == 0])
    


print(problem1())
