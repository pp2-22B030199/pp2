import math
import time

number = int(input())
second = int(input())
def square(x):
    a = math.sqrt(x)
    return a
a = second/1000
time.sleep(a)
print("Square root of", number, "after",second,"miliseconds is", square(number))