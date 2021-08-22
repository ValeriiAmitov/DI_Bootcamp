#exs1
items_list = ["humus", "cherry", "coffee"]

def add_item():
    item = input("What do you want to add in the cart?\n")
    index = int(input("At what index would you like to add it?\n"))
    items_list.insert(index, item)
    print(items_list)


add_item()


#exs2
def count_spaces():
    word = input("Write a sentence:\n")
    spaces = word.count(" ")
    print(f"The number of spaces is: {spaces}")


count_spaces()


#exs3
def count_letters():
    sentence = input("Write a sentence:\n")
    count_upper = 0
    count_lower = 0
    for word in sentence:
        if word.isupper():
            count_upper += 1
        elif word.islower():
            count_lower += 1
    print(f"The number of upper case letters is: {count_upper}")
    print(f"The number of lower case letters is: {count_lower}")


count_letters()


#exs4
def my_sum(nums_list):
    nums_sum = 0
    for item in nums_list:
        nums_sum = nums_sum + item
    print(nums_sum)


my_sum([1, 5, 4, 2])


#exs5
def find_max(nums_list):
    max_num = max(nums_list)
    print(max_num)


find_max([0, 2, 6, 70])


#exs6
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(4))