CT=float(input("Temperature in degree celcious: "))#celciuos temperature

if CT>0:
    FT=(CT*(9/5))+32
    print("Fahrenheit Temperature: ", FT, "F")#Farhenheit temp.

else:
    KT=CT+273.15
    print("Kelvin temperature: ", KT, "K")#kelvin temp.