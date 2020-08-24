#include<iostream>

using namespace std;



// 4 million Fibonacci numbers  d

int main(){
	
	/*
        int a = 0;
        int b = 1;
        int c  = a + b;
	*/

	
	long long a = 0;
	long long b = 1;
	long long c  = a + b;
	
	long sum = 0;

	//long long  n = 4000000;
	while(c<=4000000){
	


		if(c%2 == 0){
		
			sum = sum + c;
		
		}
		cout<<c<<endl;
		a=b;
		b=c;
		c=a+b;
		

		
	}

	cout<<"sum = "<<sum<<endl;

return 0;
}
