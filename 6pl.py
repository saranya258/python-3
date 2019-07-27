t,s=map(str,input().split())
if(len(t)!=len(s)):
    print("no")
else :
    f1=[t.count(j) for j in t]
    f2=[s.count(j) for j in s]
if(f1==f2):
    print("yes")
else:
    print("no")
