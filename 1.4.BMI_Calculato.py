wt = float(input("In Kg: ")) 
ht = float(input("In Metter: ")) 


BMI = wt/(ht**2)

print("BMI: ", BMI)

if BMI<=0:
    print("Invalid")
elif BMI<18.5:
    print("Under weight")
elif BMI<=24.9:
    print("Normal")
elif BMI<=29.9:
    print("Over weight")
else:
    print("Obese")