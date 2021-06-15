#include <iostream>
using namespace std;

int A[1000000];

int main() {
	int MIN = -1000001;
	int MAX = 1000001;
	int N;

	cin >> N;
	for (int i = 0; i < N; i++)
	{
		cin >> A[i];
		if (MIN < A[i]) MIN = A[i];
		if (MAX > A[i]) MAX = A[i];
	}

	cout << MAX << " " << MIN;

}