//
//  15596.cpp
//  BOJ
//
//  Created by 유수안 on 2021/06/13.
//

#include <vector>
using namespace std;

// 출력 예제가 없어서 함수만 만들면 되는 문제

long long sum(vector<int> &a)
{
    long long res=0;
    for (int i=0; i<a.size(); i++)
    {
        res=res+a[i];
    }
    return res;
    
}
