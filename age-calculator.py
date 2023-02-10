import datetime
age = int(input("Please enter your age: "))
mob = input("What is the name of the month for your birthday? : ")
mob.lower()
timenow = datetime.datetime.now()
year = int(timenow.year)

# YOB
year = year - age

# Month dictionary
months = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12
}

# Month
month = months[mob]
if month > timenow.month:
    year = year - 1

# Converts the month number to the month name
for i in months:
    if months[i] == month:
        month = i

print(f"You were born on {month} {year}")