# Python3 code to demonstrate
# attributes of now()

# importing datetime module for now()
import datetime

# using now() to get current time
current_time = datetime.datetime.now()

# Printing attributes of now().
print("The attributes of now() are : ")

print("Year : ", end="")
print(current_time.year)

print("Month : ", end="")
print(current_time.month)

print("Day : ", end="")
print(current_time.day)

print("Hour : ", end="")
print(current_time.hour)

print("Minute : ", end="")
print(current_time.minute)

print("Second : ", end="")
print(current_time.second)

print("Microsecond : ", end="")
print(current_time.microsecond)
