# Write a program using recursion to print the factorial of a number n take input from the user
def factorial(n):
    if(n == 0 or n == 1):
        return 1
    return n * factorial(n-1)

b = int(input("Enter a number :"))
print("The factorial of your number is : ", factorial(b))

# Write a program to print the fibonacci series using recursion
def fibonacci(n):
    if(n == 1 or n ==2):
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

c = int(input("Enter a number for your fibonacci series :"))
print("The fibonacci term is :" , fibonacci(c))

# write a program to find the sum of n natural number
def sum(a):
    if(a == 0):
        return 0
    return a + sum(a-1)
k = int(input("Enter the term :"))
print("The sum of all your n th term is :", sum(k))