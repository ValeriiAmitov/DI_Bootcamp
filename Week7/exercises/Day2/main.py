import random

#exs1
def message():
    print("I'm learning Python!")

message()


#exs2
def favorite_book(title):
    print(f"One of my favorite books is {title}")

favorite_book("Duna")


#exs3
def describe_city(city, country="Israel"):
    print(f"{city} is in {country}")

describe_city("Ramat Gan")


#exs4
def random_numbers(num):
    num2 = random.randrange(1, 101)
    if num == num2:
        print("Wonderful, we have a match!")
    print(f"We have a different digitals, yours is {num} AI putted this numbers: {num2}")

random_numbers(26)



#exs5
def make_shirt(size="M", message="Hakuna Matata"):
    print(f"The size of t-shitrt is {size} read a message {message}")

make_shirt("S", "LET'S WRITE A CODE")
make_shirt("L")
make_shirt("M")


#exs6
magicians = ["Konstantine", "Valerii Amitov", "Hugh Jackman"]

def show_magicians(names):
    for name in names:
        print(name)

def make_great(modify_list):
    copy_list = modify_list.copy()
    modify_list.clear()
    while len(copy_list) != 0:
        changed_name = copy_list.pop() + " the Great"
        modify_list.append(changed_name)

show_magicians(magicians)
make_great(magicians)
show_magicians(magicians)