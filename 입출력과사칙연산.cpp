#include <iostream>
using namespace std;
/* 1�ܰ� */
int main()
{

	/* 2557. Hello World */
	cout << "Hello World!" << endl;


	/* 10718. We love kriii */
	cout << "����ģ�� ��������" << endl;
	cout << "����ģ�� ��������" << endl;
	/* 10171. ����� */
	cout << "\\    /\\" << endl;
	cout << " )  ( ')" << endl;
	cout << "(  /  )" << endl;
	cout << " \\(__)|" << endl;
	/* 10172. �� */
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

	cout.precision(10); // �����θ� �����Ͽ� �Ҽ��� 10�ڸ�
	cout << a3 / b3 << endl;

	// cout << fixed; �Ҽ����� �������� ����ϰڴٴ� �ǹ�. �Ҽ��� �Ʒ��� n�ڸ���ŭ ����� �ȴ�.

	/* 10869.��Ģ���� */
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

	/* 10430.������ */
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

	/* 2588.���� */
	int a6, b6;
	cin >> a6 >> b6;
	cout << a6 * (b6 % 10) << endl;
	cout << a6 * ((b6 / 10) % 10) << endl;
	cout << a6 * (b6 / 100) << endl;
	cout << a6 * b6 << endl;
}