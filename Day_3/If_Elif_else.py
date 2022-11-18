
height = int(input("Enter a number: "))

if height >=120:
    print("Your height its ok.")
    
    age = int(input("Enter your age: "))
    if age <12:
        print("Take $5.")
    elif age <=18:
        print("Take $10.")
    elif age <=25:
        print("Take $15.")
    elif age > 26:
        print("Take $25.")
else:
    print("Your height is vfery short.")