# Another way to solve the problem 

# Calculating the last multiple of 3 and 5 below 1000
qt3 = 1000//3
lm3=3*qt3


qt5= 1000//5
lm5=qt5*5


#Idea is to add all multiples of 3 and 5 till 1000 and also subtract doubles by subtracting this sum by a sum of all multiples of 15 to negate the doubble count
qt15=1000//15
lm15=qt15*15


#Summing up
Multiple_of_3=0
sum3=0
while Multiple_of_3<lm3:
	Multiple_of_3=Multiple_of_3+3
	sum3=sum3+Multiple_of_3


Multiple_of_5=0
sum5=0
while Multiple_of_5<lm5:
	Multiple_of_5=Multiple_of_5+5
	if Multiple_of_5>=1000:
		break
	sum5=sum5+Multiple_of_5

Multiple_of_15=0
sum15=0
while Multiple_of_15<lm15:
	Multiple_of_15=Multiple_of_15+15
	sum15=sum15+Multiple_of_15


total=(sum3+sum5)-sum15

print(total)
	

