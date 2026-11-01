from datetime import date, datetime

print("===== AGE CALCULATOR =====")

dob = input("Enter your Date of Birth (DD-MM-YYYY): ")

birth_date = datetime.strptime(dob, "%d-%m-%Y").date()
today = date.today()

# Calculate age
age = today.year - birth_date.year

if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1

# Calculate next birthday
next_birthday = date(today.year, birth_date.month, birth_date.day)

if next_birthday < today:
    next_birthday = date(today.year + 1, birth_date.month, birth_date.day)

days_left = (next_birthday - today).days

print("\n===== YOUR DETAILS =====")
print("Date of Birth:", birth_date.strftime("%d-%m-%Y"))
print("Current Date:", today.strftime("%d-%m-%Y"))
print("Your Age:", age, "years")
print("Next Birthday:", next_birthday.strftime("%d-%m-%Y"))
print("Days Until Birthday:", days_left)
