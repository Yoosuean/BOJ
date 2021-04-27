#include <iostream>
using namespace std;

int main() {
	int n, x, e;
	cin >>n>> x;
	if (n < 1 || n>10000) {
		cout << "error";
		return 0;
	}
	
	for (int i = 0; i < n; i++) {
		cin >> e;
		if (e < x)
			cout << e <<" ";
	}

}