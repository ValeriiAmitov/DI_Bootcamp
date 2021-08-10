#multiplication table

num = int(input("Multiplication table. Enter your number:  "))
for i in range(1, 9):
    print(num, 'x', i, '=', num*i)