#for loops = execute a block of code  a fixed number of times
                # you can iterate over a range, string , sequence, etc

print("this is the  first for loop")

for i in range(1,11):
    print(i) 
print("this is the first for  loop in reverse")

for counter in reversed(range(1,11)):
    print(counter)
    

print("this is the  first for loop with step up2 ")

for x in range(0,21, 2):
    print(x)

# print("for loop over string")

# name = "Anubhav Jha"

# for x in name:
#     print(x)

print("for loop over string")

name = "Anubhav Jha"

for x in name:
    if x == " ":
        continue
    else:
        print(x)