N= int(input("Enter number: "))


a=0
b=1


for _ in range (N):
    print(a, end="")
    a,  b=b,  a+b

    print("fsequence: ")