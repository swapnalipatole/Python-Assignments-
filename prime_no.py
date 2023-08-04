
i = int(input("Enter Number : "))
prime = True
for j in range(2,i):
    if(i%j==0):
        prime = False
        print(j)
        break
if(prime):
    print(i," is Prime number")
else:
    print(i," is not Prime Number")