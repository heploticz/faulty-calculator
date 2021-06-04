#This calculator is designed by Saw Chin

print("Enter the first number.")
n1=int(input())
print("Enter the second number.")
n2=int(input())
print("Select the operation. +,-,*,/")
opt= input()
if n1*n2==45*3:
    print("555")
elif n1+n2==56+9:
    print("77")
elif n1/n2==56/6:
    print(4)
elif opt=="*":
    print(n1*n2)
elif opt=="+":
    print(n1+n2)
elif opt=="-":
    print(n1-n2)
elif opt=="/":
    print(n1/n2)

else:
    print("The operation is not available.")