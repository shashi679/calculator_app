
num1 =input("Enter the first number: ")
num2 = input("Enter the second number: ")

if num1.isnumeric() and num2.isnumeric():
    num1 = int(num1)
    num2 = int(num2)
    pass
else:
    print("invalid input, try again!")
    exit()

sign = input("Enter the sign: ")

if sign not in ["+", "-", "*", "/"]:
    print("invalid input, try again!")
    exit()
    
result = 0

if sign == "+":
    result = num1 + num2
elif sign == "-":
    result = num1 - num2
elif sign == "*":
    result = num1 * num2
elif sign == "/":
    if num2 != 0:
     result = num1 / num2
    else:
        print("Cannot divide by zero")
else:
    print("Invalid sign")
    
print("The result is:", result)




