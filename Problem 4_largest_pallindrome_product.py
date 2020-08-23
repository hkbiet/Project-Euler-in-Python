#!/usr/bin/env python3

'''
for i in range(100, 1000):
    print(i)
'''

# brute multiplication



def if_pallindrome(num):
    print()
    #print("INSIDE PALLIN CHECK FUNCTION & recieved \n", num)
    original = num
    temp = 0
    while(num>0):
        temp = temp + num%10
        #print("temp = temp + num%10 = {0} : ".format(temp))
        temp = temp * 10
        #print("temp = temp * 10 = {0} : ".format(temp))
        num = num // 10
        #print("num = num / 10 = {0} : ".format(num))
    temp = temp / 10

    if(temp == original):
        #print("returning TRUE , reversed = {0} and original  = {1} and stored original = {2}\n\n".format(temp, num, original))
        return True
    else:
        #print("returning FALSE , reversed = {0} and original  = {1} and stored original = {2}\n\n".format(temp, num, original))   
        return False




    


#num = int(input("ENTER NUMBER : \n"))

#if(if_pallindrome(num)):
#    return True
    #print(num, " is pallindromes\n\n")
#elif(not(if_pallindrome(num))):
#    print(num, "IS NOT PALLINDROME\n\n")


def largest_pallindrome():
    pallindrome = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            #print("\n MULTIPLYING {0} with {1} = {2}".format(i, j, i*j))
            if(if_pallindrome(i*j) and (i*j > pallindrome)):
                #print("stored pallindrome = {0} and new pallindrome is = {1}".format(pallindrome, i*j))
                pallindrome = i*j
    return pallindrome



#print("\n THE LARGEST PALLINDROME FORMED OF MULTIPLYING TWO 3 DIGIT NUMBERS IS : ", pallindrome)

if __name__ == "__main__":
	print("\n THE LARGEST PALLINDROME FORMED OF MULTIPLYING TWO 3 DIGIT NUMBERS IS : {0}".format(largest_pallindrome()) )
