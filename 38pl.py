def print_factors(x):
   for i in range(1, x + 1):
       if x % i == 0 and i%2==0:
           print(i,end=' ')
num = int(input())
print_factors(num)
