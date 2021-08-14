#Exs1
my_fav_numbers = {13, 20, 91}
my_fav_numbers.add(8)
my_fav_numbers.add(10)
my_fav_numbers.pop()
friend_fav_numbers = {2, 17, 89}

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)


#Exs2: the answer is - we cannot add more integers to the tuple


#Exs3
for digitals in range(1, 21):
    print(digitals)


#Exs4
floats_list = []
counter = 1
while counter < 5:
    counter += 0.5
    floats_list.append(counter)
print(floats_list)


# Exs5
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
print(basket)

counter = 0
for items in basket:
    if items == "Apples":
        counter += 1
print(counter)


#Exs6
my_name = "Valerii"
some_username = " "
while some_username != my_name:
    some_username = input("What's your name, buddy? ")


#Exs7
some_actions = ["running", "moving", "writing", "listening", "watching",]
for item in some_actions:
    if int(some_actions.index(item)) % 2 == 0:
        print(item)



#Exs8
for nums in range(1500, 2501):
    if (nums % 5) == 0:
        print(nums)
    elif (nums % 7) == 0:
        print(nums)



#Exs9
your_fruits = input("So, what's your favorite fruits?: ")
list(your_fruits)
some_fruit = input("Can you write some fruit here?: ")
if some_fruit in your_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy")


#Exs10
toppings = []
new_topping = " "
total = 10

while new_topping != "quit":
    new_topping = input("which topping do you want to add, stop letter 'quit': ")
    toppings.append(new_topping)
    total += 2.5
    print("Your topping was added, more topping?")

toppings.pop() #let's quit from the list
print("Let's see what you got: ")
for item in toppings:
    print(item)
print(f"open your wallet, the final price is: {total - 2.5 }")

#Exs11
total = 0
online = True
while online:
    age = input("Type age of person to buy our tickets. Type 'quit' when you'll finished: ")
    if age == "quit":
        online = False
    elif int(age) < 3:
        total += 0
    elif 3 <= int(age) <= 12:
        total += 10
    elif int(age) > 12:
        total += 15

print(f"The final price of your tickets is: {total}")

teenager= []
online = True
while online:
    name = input("Type your name. When you are finished type 'quit': ")
    if name == "quit":
        online = False
        break
    age = input("Write your age: ")
    if int(age) > 21:
        teenager.append(name)
print(f"Who can see this movies: {teenager}")


#Exs12
names = ["Nikole", "Michael", "Don", "Loren", "Valerii", "Natalia"]
for name in names:
    age = input(f"Your age {name}? ")
    if int(age) < 16:
        names.remove(name)
print(names)


#Exs13
sandwich_orders = ['Potato sandwich', 'Pastrami sandwich', 'Organic sandwich', 'Asian Sandwich']
ready_sandwiches = []
for item in sandwich_orders:
    ready_sandwiches.append(item)
    print(f"Your {item} is ready!")


#Exs14
print("The deli has run out of pastrami")
lost_sandwich = "Pastrami Sandwich"
while lost_sandwich in sandwich_orders:
    sandwich_orders.remove((lost_sandwich))
while lost_sandwich in ready_sandwiches:
    ready_sandwiches.remove(lost_sandwich)
print(sandwich_orders)
print(ready_sandwiches)