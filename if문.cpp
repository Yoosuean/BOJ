#include<iostream>
using namespace std;
/* 2단계 */
int main(void) {
	/* 1330. 두 수 비교하기 */
		int a, b;
		cin >> a >> b;

		if (a > b)
			cout << ">";
		else if (a < b)
			cout << "<";
		else if (a == b)
			cout << "==";

	/* 9498. 시험 성적 */
		int c;
		cin >> c;
		
			if (c>=90)
				cout << "A";
			else if (c>=80)
				cout << "B";
			else if (c>=70)
				cout << "C";
			else if (c>=60)
				cout << "D";
			else
				cout << "F";

	/* 2753. 윤년 */
			int d;
			cin >> d;

			if (d % 4 == 0)
				if (d % 100 != 0 || d % 400 == 0)
					cout << "1";
				else
					cout << "0";
			else
				cout << 0;

	/* 14681. 사분면 고르기 */
			int a2, b2;
			cin >> a2 >> b2;

			if (a2 > 0)
				if (b2 > 0)
					cout << "1";
				else
					cout << "4";
			else
				if (b2 > 0)
					cout << "2";
				else
					cout << "3";

	/* 2884. 알람시계 */
			int h, m;
			cin >> h >> m;

			if (m >= 45)
				m -= 45;
			else {
				m+= 15;
				h--;
			}
			if (h < 0)
				h = 23;

				cout << h << " " << m;
}