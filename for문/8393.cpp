#include<iostream>
using namespace std;
/* 3�ܰ� */

int main() {

	/* 8393. �� */
	int n;
	int sum= 0;
	cin >> n;

	while(0<=n)
	{
		sum +=n;
		n--;
	}
	cout << sum;

}