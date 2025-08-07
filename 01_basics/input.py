#use of input() function same as cin>>
# but input return the entered data in form of string so to use intreger we first have to do type casting to the input varible


name =input("hey what is you Name! : ")
age=int(input("how old are you : "))
# age = int(age)
age = age+1
print( f"hey {name}, Nice to meet you")
print(f"I'm too {age} years old")