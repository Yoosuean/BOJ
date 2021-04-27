#include<iostream>
using namespace std;

int main()
{
	int a, b, res;

	cin >> a;
	b = 1;

	while (b <= 9)
	{
		res = a * b;
		cout << a << " * "<< b << " = " << res << "\n";
		b++;
	}
}