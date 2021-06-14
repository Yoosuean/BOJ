//
//  10872.cpp
//  BOJ
//
//  Created by 유수안 on 2021/06/14.
//


#include <iostream>
using namespace std;

int factorial(int n)
{
    if(n<=1)
        return 1;
    
    return n*factorial(n-1); // 재귀 함수
}

int main()
{
    int num;
    cin>>num;
    
    cout<<factorial(num)<<"\n";
    
}
