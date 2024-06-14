import numpy as np
import pandas as p
import matplotlib as mp

# Question 1:
sum = 0
for x in range(1000):
    if(x % 3 == 0 or x % 5 ==0):
        sum += x
print(sum)


# Question 2:
a = 1
b = 2
sum = 2
while(b < 4000000):
    fib = a + b
    a = b
    b = fib
    if (b % 2 == 0):
        sum += b
print(sum)
