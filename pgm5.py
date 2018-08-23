n1,n2,n3=input().split()
if (n1>n2) and (n1>n3):
	num=n1
elif (n2>n3) and (n2>n1):
            num=n2	
else:
            num=n3								
print(num)
