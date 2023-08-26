a=18
b=24
c=min(a,b)
for i in range(c,0,-1):
    if(a%i==0 and b%i==0):
        print(i)
        break
    
