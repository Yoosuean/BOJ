//
//  10870.cpp
//  BOJ
//
//  Created by 유수안 on 2021/06/14.
//

#include <iostream>
using namespace std;

int fivo(int n)
{
    if(n==0) return 0;
    if(n==1) return 1;
    return fivo(n-2)+fivo(n-1);
    
}

int main()
{
    int num;
    cin>>num;
    cout<<fivo(num)<<endl;
}

