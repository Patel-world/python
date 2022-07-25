e=0
even=[]

for i in range(1000,3001):
   
    for j in str(i):
        k=int(j)
        
        if(k%2==0):
           
            e=e+1

    if(e==4):
        #print(i)
        even.append(i)
        
    e=0



print(even)