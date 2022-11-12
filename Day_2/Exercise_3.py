
# Live in Weeks

age = input("What is your current age? ")

age_as_int = int(age)

years = 90 - age_as_int
days = years * 365
weeks = years * 52
months = years * 12
print(f"You have\n{days} days\n{weeks} weeks\n{months} months left")