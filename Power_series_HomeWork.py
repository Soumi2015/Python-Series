base = int(input("Enter the base number: "))
n = int(input("Enter the number of terms: "))

print("Power Series:")

for i in range(1, n+1):
    print(base, "^", i, "=", base ** i)