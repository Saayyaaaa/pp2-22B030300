#exercise 1

print("Hello, World!")


#exercise 2

if 5 > 2:
    print("Five is greater than two!")


#exercise 3

#This is a comment


#exercise 4

"""
This is a comment
written in 
more than just one line
"""


#exercise 5

carname = "Volvo"


#exercise 6

x = 50


#exercise 7

x = 5
y = 10
print (x + y)


#exercise 9

x = 5
y = 10
z = x + y
print(z)


#exercise 10

myfirst_name = "John"


#exercise 11

x = y = z = "Orange"


#exercise 12

def myfunc():
global x
    x = "fantastic"


#exercise 13

x = 5
print(type(x))

int


#exercise 14

x = "Hello World"
print(type(x))

str


#exercise 15

x = 20.5
print(type(x))

float


#exercise 16

x = ["apple", "banana", "cherry"]
print(type(x))

list


#exercise 17

x = ("apple", "banana", "cherry")
print(type(x))

tuple


#exercise 18

x = {"name" : "John", "age" : 36}
print(type(x))

dict


#exercise 19

x = True
print(type(x))

bool


#exercise 20

x = 5
x = 
float (x)


#exercise 21

x = 5.5
x = 
int (x)


#exercise 22

x = 5
x = 
complex (x)


#exercise 23

x = "Hello World"
print(len(x))


#exercise 24

txt = "Hello World"
x = txt[0]


#exercise 25

txt = "Hello World"
x = txt[2:5]


#exercise 26

txt = " Hello World "
x = txt.strip()


#exercise 27

txt = "Hello World"
txt = txt.upper()


#exercise 28

txt = "Hello World"
txt = txt.lower()


#exercise 29

txt = "Hello World"
txt = txt.replace("H", "J")


#exercise 30

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))


#exercise 31

print(10 > 9)

True


#exercise 32

print(10 == 9)

False


#exercise 33

print(10 < 9)

False


#exercise 34

print(bool("abc"))

True


#exercise 35

print(bool(0))

False


#exercise 36

print(10 * 5)


#exercise 37

print (10 / 2)


#exercise 38

fruits = ["apple", "banana"]
if "apple" in fruits:
    print("Yes, apple is a fruit!")


#exercise 39

if 5 != 10:
    print("5 and 10 is not equal")


#exercise 40

if 5 == 10 or 4 == 4:
    print("At least one of the statements is true")


#exercise 41

fruits = ["apple", "banana", "cherry"]
print(fruits[1])


#exercise 42

fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"


#exercise 43

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")


#exercise 44

fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")


#exercise 45

fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")


#exercise 46

fruits = ["apple", "banana", "cherry"]
print(fruits[-1])


#exercise 47

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])


#exercise 48

fruits = ["apple", "banana", "cherry"]
print(len(fruits))


#exercise 49

fruits = ("apple", "banana", "cherry")
print(fruits[0])


#exercise 50

fruits = ("apple", "banana", "cherry")
print(len(fruits))


#exercise 51

fruits = ("apple", "banana", "cherry")
print(fruits[-1])


#exercise 52

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])


#exercise 53

fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
    print("Yes, apple is a fruit!")


#exercise 54

fruits = {"apple", "banana", "cherry"}
fruits.add("orange")


#exercise 55

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)


#exercise 56

fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")


#exercise 57

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")


#exercise 58

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))


#exercise 59

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020


#exercise 60

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"

#exercise 61

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")


#exercise 62

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()


#exercise 63

a = 50
b = 10
if a > b:
    print("Hello World")


#exercise 64

a = 50
b = 10
if a != b:
    print("Hello World")


#exercise 65

a = 50
b = 10
if a == b:
  print("Yes")
else:
  print("No")


#exercise 66

a = 50
b = 10
if a == b:
    print("1")

elif a > b:
    print("2")

else:
    print("3")


#exercise 67

if a == b and c == d:
  print("Hello")


#exercise 68

if a == b or c == d:
  print("Hello")


#exercise 69

if 5 > 2:
    print("Five is greater than two!")


#exercise 70

if 5 > 2: print("Five is greater than two!")


#exercise 71

print("Yes") if 5 > 2 else print("No")


#exercise 72

i = 1
while i < 6:
  print(i)
  i += 1


#exercise 73

i = 1
  while i < 6:
    if i == 3:
        break
    i += 1


#exercise 74

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)


#exercise 75

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")


#exercise 76

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)


#exercise 77

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


#exercise 78

for x in range(6):
    print(x)


#exercise 79

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)


#exercise 80

def my_function():
  print("Hello from a function")


#exercise 81

def my_function():
  print("Hello from a function")

my_function()


#exercise 82

def my_function(fname, lname):
  print(fname)


#exercise 83

def my_function(x):
    return x + 5


#exercise 84

def my_function(*kids):
  print("The youngest child is " + kids[2])


#exercise 85

def my_function(**kid):
  print("His last name is " + kid["lname"])


#exercise 86

x = lambda a : a


#exercise 87

class MyClass:
  x = 5


#exercise 88

class MyClass:
  x = 5

p1 = MyClass()

#exercise 89

class MyClass:
  x = 5

p1 = MyClass()

print(p1.x)


#exercise 90

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age


#exercise 91

class Student(Person):


#exercise 92

class Person:
  def __init__(self, fname):
    self.firstname = fname

  def printname(self):
    print(self.firstname)

class Student(Person):
  pass

x = Student("Mike")
x.printname()


#exercise 93


import mymodule


#exercise 94

import mymodule as mx


#exercise 95

import mymodule
print(dir(mymodule))


#exercise 96

from mymodule import person1