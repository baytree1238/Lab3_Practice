"""
Program that accepts an integer value
and prints out the name of the corresponding day

"""

day_number = int(input("Enter the day number: "))

if day_number == 1:
    print(f"Day {day_number} is Monday.")
elif day_number == 2:
    print(f"Day {day_number} is Tuesday.")
elif day_number == 3:
    print(f"Day {day_number} is Wednesday.")
elif day_number == 4:
    print(f"Day {day_number} is Thursday.")
elif day_number == 5:
    print(f"Day {day_number} is Friday.")
elif day_number == 6:
    print(f"Day {day_number} is Saturday.")
elif day_number == 7:
    print(f"Day {day_number} is Sunday.")
else:
    print("Invalid day.")

"""
Program that asks the user to enter a year,
and displays the month and day for Easter Sunday on that year.

"""

year = int(input("Enter the year: "))

a = year%19
b = year//100
c = year%100
d = b//4
e = b%4
f = (b+8)//25
g = (b-f+1)//3
h = (19*a + b - d - g + 15)%30
i = c//4
k = c%4
m = (32 + 2*e + 2*i - h - k) % 7
n = (a + 11*h + 22*m) // 451

month = int((h + m - 7*n + 114) // 31)
day = int(1 + (h + m - 7*n + 114)%31)

print(f"In {year}, Easter will occur on day {day} of month {month}")


"""
This program is similar to above, but it displays the name of the month
instead of the number.
"""

year = int(input("Enter the year: "))

a = year%19
b = year//100
c = year%100
d = b//4
e = b%4
f = (b+8)//25
g = (b-f+1)//3
h = (19*a + b - d - g + 15)%30
i = c//4
k = c%4
m = (32 + 2*e + 2*i - h - k) % 7
n = (a + 11*h + 22*m) // 451

month = int((h + m - 7*n + 114) // 31)
if month == 1:
    month = "Janurary"
elif month == 2:
    month = "Feburary"
elif month == 3:
    month = "March"
elif month == 4:
    month = "April"
elif month == 5:
    month = "May"
elif month == 6:
    month = "June"
elif month == 7:
    month = "July"
elif month == 8:
    month = "August"
elif month == 9:
    month = "September"
elif month == 10:
    month = "October"
elif month == 11:
    month = "November"
elif month == 12:
    month = "December"
else:
    None


day = int(1 + (h + m - 7*n + 114)%31)


print(f"Easter will occur on {day} {month}, {year}.")



"""
This program asks the user to enter the name of a day, and determine
if is it a working day or a weekend day.
"""

day = input("Enter the name of a day: ")

if day in "Monday""Tuesday""Wednesday""Thursday""Friday":
    day_type = "working"
elif day in "Saturday""Sunday":
    day_type = "weekend"
else:
    day_type = "wrong"

print(f"{day} is a {day_type} day.")


"""
This program asks the user to enter the denomination and displays the person and
description, with the exact formatting/spelling showin in the table above. 
"""

denomination = int(input("Enter the denomination: "))

if denomination == 5:
    person = "Sir Edmund Hillary"
    description = "a mountaineer"
elif denomination == 10:
    person = "Kate Sheppard"
    description = "a suffragette"
elif denomination == 20:
    person = "Queen Elizabeth II"
    description = "the former monarch of New Zealand"
elif denomination == 50:
    person = "Sir Āpirana Ngata"
    description = "a Māori politician"
elif denomination == 100:
    person = "Ernest Rutherford"
    description = "a physicist"
else:
    person = None
    description = None


print(f"${denomination} shows {person} who is famous as {description}.")


"""
This program reads a year from the user and displays a message indicating
wheter or not it is a leap year.
"""

year = int(input("Enter the year: "))

if year%400 == 0:
    year_type = "a leap year"
elif year %100 == 0:
    year_type = "not a leap year"
elif year%4 == 0:
    year_type = "a leap year"
else:
    year_type = "not a leap year"

print(f"{year} is {year_type}")


















































