def add(a, b):
    return a + b 
def sub(a, b):
    return a - b 
def multiply(a, b):
    return a * b 
def divide(a, b):
    if b==0:
        return "Error: can't divide by zero!"
    return a/b



opt = input("Choose your operater(+, -, *, /): ")
x = float(input("Enter your 1st num: "))
y = float(input("Enter your 2nd num: "))

if opt == '+':
    print("result:", add(x, y))
elif opt== '-':
    print("result:", sub(x, y))
if opt == '*':
    print("result:", multiply(x, y))
elif opt== '/':
    print("result:", divide(x, y))
else:
    print("Invalid Operation")