#include <iostream>
using namespace std;

int main()
{
	int a, b, c;
	int arr[10] = { 0 }; //�ʱ�ȭ
	int sum;

	cin >> a >> b >> c;
	sum = a * b * c;

	while (sum > 0)
	{
		arr[sum % 10]++;
		sum /= 10;
	}

	for (int i = 0; i <10; i++)
	{
		cout << arr[i] << endl;
	}


}