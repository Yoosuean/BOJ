#include<iostream>
#include<string>

using namespace std;

int main()
{
	string s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ", input;
	int arr[26] = { 3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10 };
	int sum = 0;
	cin >> input;
	for (int i = 0; i < input.length(); i++)
	{
		sum += arr[(int)s[(int)input[i] - 65] - 65];
	}

	cout << sum;
	return 0;
}