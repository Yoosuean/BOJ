#include <iostream>
using namespace std;

int main() {

	int num;
	float score[1000];
	cin >> num;

	for (int i = 0; i < num; i++)
	{
		cin >> score[i];
	}

	int max = 0;
	for (int i = 0; i < num; i++)
	{
		if (score[i] > max)
			max = score[i];
	}


	for (int i = 0; i < num; i++)
	{
		score[i] = score[i] / max * 100;
	}

	float total = 0;
	for (int i = 0; i < num; i++)
	{
		total += score[i];
	}

	cout << fixed;
	cout.precision(2);
	cout << total / num << endl;

	return 0;
}