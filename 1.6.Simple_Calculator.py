num1=int(input("Enter any nymber: "))
num2=int(input("Enter any number: "))
op=input("Enter an operator: ")

if op=='+':
    SR= num1+num2
    print("Sum: ", SR)
elif op=='-':
    StR= num1-num2
    print("Substraction: ", StR)
elif op=='*':
    MR= num1*num2
    print("Multifly:",MR)
else:
    if num2!=0:
        DR=num1/num2
        print("Division: ",DR)
    else:
        print("Error") #division by zero is not allowed
