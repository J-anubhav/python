# nested loop = loop within another loop 
#           outer loop:
    #           inner loop: 


# for counter in range(3):
#     for x in range (1,11):
#         print(x, end =" ")
    
#     print()


rows = int(input("Enter the numer of rows: "))
coloums = int(input("Enter the numer of Colums: "))
symbol = input("Enter a symbol to use: ")

for counter in range(rows):
    for x in range (coloums):
        print(symbol, end =" ")
    
    print()