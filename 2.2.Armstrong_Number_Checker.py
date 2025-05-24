num=int(input("input any number: "))

#convert ditgit to number & count
digits=str(num)
count=len(digits)

# Calculate the Armstrong sum using a for loop

i=0

for digit in digits:
    i+=int(digit)**count
#check
if i==num:
    print("This is an armstrong number")

else:
    print("This is not an armstrong number")