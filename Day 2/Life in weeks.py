age = input("What is your current age? ")
age_as_int = int(age)
total_days = (90*365 - age_as_int*365)
total_weeks = (90*52 - age_as_int*52)
total_months = (90*12 - age_as_int*12)

print(f"You have {total_days} days, {total_weeks} weeks, and {total_months} months left.")