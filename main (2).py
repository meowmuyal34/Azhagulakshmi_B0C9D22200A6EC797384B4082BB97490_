# Take user input to calculate factorial
num = int(input("Enter a number: "))
factorial = 1

# Check if the input is negative, positive or zero
if num < 0:
    print("Factorial of negative value is not defined")
elif num == 0:
     print("Factorial of  0 is ‘1’")
else:
    for i in range(1, num+1):
        factorial *= i
    print("The factorial of", num, "is", factorial)
  