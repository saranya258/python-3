v11,v21=map(int,input().split())
v31=[]
for k in range(v11,v21+1):
    for p in range(2,k):
        if(k%p==0):
            break
    else:
        v31.append(k)
print(len(v31))
