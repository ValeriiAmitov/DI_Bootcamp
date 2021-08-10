# Exs1
print("Hello World " * 4)

# Exs2
calcul = (99**3) * 8
print(calcul)

# Exercise 3
# >>> 5 < 3 --> False
# >>> 3 == 3 --> True
# >>> 3 == "3" --> False
# >>> "3" > 3 --> Error
# >>> "Hello" == "hello" --> False

# Exs4
computer_brand = "Apple"
print(f"I have a {computer_brand} computer")

# Exs5
name = "Valerii"
age = 30
shoe_size = 43
info = f"My name is {name}, I'm {age} years old and my shoe size is {shoe_size}"
print(info)

# Exs6
a = 20
b = 15
if a > b:
    print("Hello world")

# Exs7
number = input("Write number, please: ")
if int(number) % 2 == 0:
    print("This number is even")
else:
    print("This number is odd")

# Exs8
my_name = "Valerii"
user_name = input("What is your name? ")
if my_name == user_name:
    print("Had we met in parallel universe before?")

# Exs9
user_heigth = input("Can you write your height in inches?: ")
if int(user_heigth) > 145:
    print("Yeep - you are tall enough to ride this Tesla")
else:
    print("Nope, looks like you need to grow up a little to ride this car")