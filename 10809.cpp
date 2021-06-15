#include <iostream>
#include<string>
using namespace std;

int main()
{
	string str;
	string alpha = "abcdefghijklmnopqrstuvwxyz";
	
	cin >> str;
	
	for (int i = 0; i < alpha.length(); i++)
	{
		cout << (int)str.find(alpha[i]) << " ";
	}
	return 0;
}