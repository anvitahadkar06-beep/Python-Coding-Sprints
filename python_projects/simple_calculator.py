#Create a calculator capable of performing addition, substraction, multiplication, division operations on two numbers.
#Program should format the output in a readable manner.

a=int(input("Enter a number"))
b=int(input("Enter another number"))

#Arthimetic Operations
print("The addition of 2 numbers is",(a+b))
print("The substraction of 2 numbers is",(a-b))
print("The multiplication of 2 numbers is",(a*b))
if b==0:
    print("Error! Division by zero is not possible")
else:
    print("The division of 2 numbers is",(a/b))
