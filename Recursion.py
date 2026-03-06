a = int(input("Enter a number : "))
if a<1 :
    print("Factorial doesn't exist or negetive numbers..")
else:
    fact = 1
    for i in range(1, a+1):
        fact = fact*i
print("The factorial is :",fact)