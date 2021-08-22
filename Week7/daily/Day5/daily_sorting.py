someWords = input("Please, write some words to separated by comas: ")
someWords_list = someWords.split(",")
someWords_list.sort()

print(f"The sorted order is: {someWords_list}")