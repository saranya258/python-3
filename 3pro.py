n=int(input())
revt=0
while(n>0):
  dig=n%10
  revt=revt*10+dig
  n=n//10
print(revt)
