#Powerof2
def isPowerOfTwo(n): 
	if (n == 0): 
		return False
	while (n != 1): 
			if (n % 2 != 0): 
				return False
			n = n // 2
	return True
# Driver code 
i=int(input())
if(isPowerOfTwo(i)): 
	print('Yes') 
else: 
	print('No') 
 

 
