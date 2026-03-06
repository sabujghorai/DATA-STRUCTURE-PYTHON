a = int(input("Enter a number : "))
fact = 1
if a < 0:
    print("Factorial doesn't exist for negative numbers.")
else:
    for i in range(1, a + 1):
        fact = fact * i
    print("The factorial is:", fact)
    