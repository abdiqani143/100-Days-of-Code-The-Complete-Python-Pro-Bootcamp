import sys
print(sys.version)

height = input("Enter yor height in m: ")
weight = input("Enter yor weight in kg: ")

bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)