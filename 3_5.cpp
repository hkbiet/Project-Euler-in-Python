#include<iostream>
using namespace std;


int main(){


	int input;
	cout<<"\nENTER THY NUMBER\n";
	cin>>input;
	int sum = 0;

	while(input){
	
		if(input%3==0){
			sum = sum + input;
		
		}else if(input%5==0){
		
			sum = sum + input;
		}
	
	
	input--;
	}

	cout<<sum<<endl;




return 0;
}
