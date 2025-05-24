age=int(input("Enter any age: "))

if age<0:
    print("Invalid")
elif age<=1:
    print("Infant")
elif age<=3:
    print("Toddler")
elif age<=12:
    print("child")
elif age<=19:
    print("Teenager")
else:
    print("Adult")