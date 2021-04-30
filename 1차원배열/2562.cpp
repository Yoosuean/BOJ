#include <iostream>
using namespace std;

int main()
{
	int index = 0;
	int max = 0;
	int num[9];

	for (int i = 0; i < 9; i++)
	{
		cin>> num[i];
		if (num[i] >= max)
		{
			max = num[i];
			index = i;
		}
	}

	cout << max << "\n" << index + 1;

}