def factorial(n):
    if(n == 0 or n == 1):
        return 1
    return n * factorial(n-1)

b = int(input("Enter a number :"))
print("The factorial of your number is : ", factorial(b))