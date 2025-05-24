#Largest among Three Numbers

num1= int(input("Enter any number: "))
num2= int(input("Enter any number: "))
num3= int(input("Enter any number: "))


if num1>num2 and num1>num3:
    print("The largest Number is: ", num1)
elif num2>num3 and num2>num1:
    print("The largest Number is: ", num2)
else:
    print("The largest Number is: ", num3)