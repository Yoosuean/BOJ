#include <iostream>
using namespace std;
/* 1단계 */
int main()
{

	/* 2557. Hello World */
	cout << "Hello World!" << endl;


	/* 10718. We love kriii */
	cout << "강한친구 대한육군" << endl;
	cout << "강한친구 대한육군" << endl;
	/* 10171. 고양이 */
	cout << "\\    /\\" << endl;
	cout << " )  ( ')" << endl;
	cout << "(  /  )" << endl;
	cout << " \\(__)|" << endl;
	/* 10172. 개 */
	cout << "|\\_/|" << endl;
	cout << "|q p|   /}" << endl;
	cout << "( 0 )\"\"\"\\" << endl;
	cout << "|\"^\"`    |" << endl;
	cout << "||_/=\\\\__|" << endl;
	/* 1000. A+B */
	int a, b;
	cin >> a >> b;
	cout << a + b << endl;
	/* 1001.A-B */
	int a1, b1;
	cin >> a1 >> b1;
	cout << a1 - b1 << endl;
	/* 10998.AxB */
	int a2, b2;
	cin >> a2 >> b2;
	cout << a2 * b2 << endl;
	/* 1008.A/B */
	double a3, b3;

	while (1) {
		cin >> a3 >> b3;
		if (a3 > 0 && b3 < 10 && b3 != 0)
			break;
		else
			continue;
	}

	cout.precision(10); // 정수부를 포함하여 소수점 10자리
	cout << a3 / b3 << endl;

	// cout << fixed; 소수점을 고정시켜 출력하겠다는 의미. 소수점 아래로 n자리만큼 출력이 된다.

	/* 10869.사칙연산 */
	int a4, b4;

	while (1) {
		cin >> a4 >> b4;
		if (1 <= a4 <= 10000 && 1 <= b4 <= 10000)
			break;
		else
			continue;
	}

	cout << a4 + b4 << endl;
	cout << a4 - b4 << endl;
	cout << a4 * b4 << endl;
	cout << a4 / b4 << endl;
	cout << a4 % b4 << endl;

	/* 10430.나머지 */
	int a5, b5, c5;

	while (1) {
		cin >> a5 >> b5 >> c5;
		if (2 <= a5 <= 10000 && 1 <= b5 <= 10000 && 1 <= c5 <= 10000)
			break;
		else
			continue;
	}

	cout << (a5 + b5) % c5 << endl;
	cout << ((a5 % c5) + (b5 % c5)) % c5 << endl;
	cout << (a5 * b5) % c5 << endl;
	cout << ((a5 % c5) * (b5 % c5)) % c5 << endl;

	/* 2588.곱셈 */
	int a6, b6;
	cin >> a6 >> b6;
	cout << a6 * (b6 % 10) << endl;
	cout << a6 * ((b6 / 10) % 10) << endl;
	cout << a6 * (b6 / 100) << endl;
	cout << a6 * b6 << endl;
}