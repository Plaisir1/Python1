import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))

except ValueError:
    print("Invalid input")

try:
    result = x /y

except ZeroDivisionError:
    print("Error: Connot divide by 0.")
    sys.exit(1)

print(f"{x} /{y} = {result}")