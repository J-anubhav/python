# while loop execute some code WHILE some condiito is true  

name = input("enter Your name: ")

while name == "":
    print("You did not enter your name")
    name = input("enter Your name: ")

print(f"hello {name}!")


age = int(input("Enter you age: "))
while age<0:
    print("Your are not born yet")
    age = int(input("Enter you age: "))

print(f"you are  {age}! year old ")


food = input('Enter a food you like (q to quit)')

while not food == 'q':
    print(f"YOu like {food}")
    food = input ("Enter anotherfood you like (q to quit)")

print("bye")


num = int(input("Enter a number between 1-10: "))

while num<1 or num >10:
    print(f"{num} is not valid")
    num = int(input("Enter a number between 1-10: "))

print(f"you number is {num}")



