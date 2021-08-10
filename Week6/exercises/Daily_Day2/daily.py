#part1
import random
user_String = input("Write a string. It must be 10 letters long: ")
string_length = len(user_String)
if string_length < 10:
    print("String not long enough")
    exit()
elif string_length > 10:
    print("String too long")
    exit()

#part2
print("The first character is: ", user_String[0], "and the last character is: ", user_String[string_length-1])

#part3
const = ""
for x in user_String:
    const += x
    print(const)

#part 4
shuffleString = " ".join(random.sample(user_String, len(user_String)))
print("Shuffle mode is activated: ", shuffleString)