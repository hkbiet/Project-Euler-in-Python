#Print out the prime numbers:

'''
 print("INPUT>>>>")
 num = input()
 for i in range(2, num+1):
	for j in range(2,i):
		if(i % j == 0):
			i = i / j
			break
	else:
 		# Prime found!
		if(num % i == 0 ):
			found = i
 print(found)

'''


num = 600851475143
#num = 13195
i=2
while(i < num/2):
	if(num % i ==0):
		num = num / i
	i = i + 1

print(num)
