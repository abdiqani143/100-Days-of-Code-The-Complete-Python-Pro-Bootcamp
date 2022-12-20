import  random
letters = [ 'a' ,'b' ,'c','d','e','f','g','h','i','j','k','l','m','n','o','p',
            'q','r','s','t','u','v','w','x','y','z',
            'A', 'B', 'C', 'D', 'E','F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N','O', 'P', 'Q', 'R','S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','*','(','-','_','+','/','?','@']
print("Welcome To The Password Generator")
letter = int(input("how many letters would you like in your password?\n"))
number = int(input("how many numbers would like?\n"))
symbol = int(input("how many letters would like?\n"))
password_list = []
for char in range(1,letter + 1):
    password_list.append(random.choice(letters))
for char in range(1,number + 1):
    password_list +=random.choice(numbers)
for char in range(1,symbol + 1):
    password_list +=random.choice(symbols)
password =""
for char in password_list:
    password  +=char
print(f"Your Password is: {password}")
