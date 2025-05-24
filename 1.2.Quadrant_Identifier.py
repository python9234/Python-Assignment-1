#x,y
x = float(input("Enter the x-coordinate: "))
y = float(input("Enter the y-coordinate: "))

if x>0 and y>0:
    coor=1
elif x<0 and y>0:
    coor=2
elif x<0 and y<0:
    coor=3
elif x>0 and y<0:
    coor=4
else:
    coor=0

print("The coordinator:", coor)