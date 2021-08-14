import datetime

birthday = input("How old are you? Please enter your birthday by format DD-MM-YYY: ")
format_date = datetime.datetime.strptime(birthday, "%d-%m-%Y")
today = datetime.datetime.now()
currentYear = today.year
age = currentYear - (format_date.year)
candles = ("i" * age)
if age == 53:
    candles = "i" * 3
print(f'''
       __{candles}__
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
''')