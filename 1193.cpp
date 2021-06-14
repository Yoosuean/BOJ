//
//  1193.cpp
//  BOJ
//
//  Created by 유수안 on 2021/06/14.
//

#include <iostream>
using namespace std;

int main() {
    int X;
    cin >> X;
    
    // 대각선 구하기
    int i =1;
    while(X>=i){
        X-=i;
        i++;
    }
    
    if(i%2==0) // 짝수일 시
    {
        cout<<X<<"/"<<i+1-X<<endl;
    }
    else // 홀수일 시
        cout<<i+1-X<<"/"<<X<<endl;
    
}
