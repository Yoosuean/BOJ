#include <iostream>
using namespace std;

int main()
{
	int n, sum = 0;
	char str;
	cin >> n;

	for (int i = 0; i < n; i++)
	{
		cin >> str;
		sum += str - 48;
	}

	cout << sum;

}