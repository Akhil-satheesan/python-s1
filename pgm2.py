a= int(input("Enter First Number:"))
b= int(input("Enter Second Number:"))
c= int(input("Enter Second Numvbe:"))
if(a>b and a>c):
   print(f"{a}is greatest Number")
   n=a
elif(b>c):
   print(f"{b} greatest Number")
   n=a
else:
   print(f"{c} is greatest Number")
   n=a
print(n+(n**2)+(n**3))
area=3.14*n**2
print(f"Area:{area}")
pmeter=2*3.14*n
print(f"Parameter:{pmeter}")