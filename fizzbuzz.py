import time
import array
from decimal import *
getcontext().prec = 64
max_range = 1_000_000

## -- JYE'S CODE START -- ##
start1 = Decimal(time.time())
fizz_buzz1 = [
    i if i%3 != 0 and i%5 != 0 else
    "FizzBuzz" if i%3 == 0 and i%5 == 0 else
    "Fizz" if i%3 == 0 else
    "Buzz" if i%5 == 0 else
    i for i in range(1, max_range)]
stop1 = Decimal(time.time())

print(stop1 - start1)
print("--test1--")
print(type(fizz_buzz1))
print("")

start2 = Decimal(time.time())
fizz_buzz2 = ["Fizz"*(not i%3) + "Buzz"*(not i%5) or i for i in range(1, max_range)]
stop2 = Decimal(time.time())
## -- JYE'S CODE END -- ##

print(stop2 - start2)
print("--test2--")
print(type(fizz_buzz2))
print("")

## -- JOHN'S CODE START -- ##
start3 = Decimal(time.time())
i = 1
fizz_buzz3 = []
while i <= max_range:
    if i % 5 == 0 and i % 3 == 0:
        #print("FizzBuzz")
        fizz_buzz3.append("FizzBuzz")
    elif i % 5 == 0:
        #print("Buzz")
        fizz_buzz3.append("Buzz")
    elif i % 3 == 0:
        #print("Fizz")
        fizz_buzz3.append("Fizz")
    else:
        #print(i)
        fizz_buzz3.append(i)
    i = i + 1
stop3 = Decimal(time.time())
## -- JOHN'S CODE END -- ##

print(stop3 - start3)
print("--test3--")
print(type(fizz_buzz3))
print("")

## -- SEE IF ALL MATCH -- ##
if(fizz_buzz1 == fizz_buzz2):
    print("1&2: TRUE")
if(fizz_buzz2 == fizz_buzz3):
    print("2&3: TRUE")
if(fizz_buzz1 == fizz_buzz3):
    print("1&3: TRUE")
else:
    print("FALSE")
## -- SEE IF ALL MATCH -- ##

## -- MORGAN'S CODE START -- ##
start4 = Decimal(time.time())
fizz_buzz4 = ""
i = 0
while(i <= max_range):
        if (i % 3 == 0 and i % 5 == 0):
            fizz_buzz4 = fizz_buzz4 + "FizzBang, "
        elif (i % 3 == 0):
            fizz_buzz4 = fizz_buzz4 + "Fizz, "
        elif(i% 5 == 0):
            fizz_buzz4 = fizz_buzz4 + "Bang, "
        else:
            fizz_buzz4 = fizz_buzz4 + str(i) + ", "
        i = i + 1
stop4 = Decimal(time.time())
## -- MORGAN'S CODE END -- ##

print(stop4 - start4)
print("--test4--")
print(type(fizz_buzz4))
