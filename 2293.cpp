//
//  2293.cpp
//  BOJ
//
//  Created by 유수안 on 2021/06/13.
//

#include <iostream>
using namespace std;

int main()
{
    int n;
    cin>>n;
    
    int layer=1; //칸 수
    int range=1; //범위
    int tmp=1;
    
    while(1)
    {
        if(range>=n)
        {
            break;
        }
        tmp=6*layer;
        layer++;
        range+=tmp;
    }
    
    cout<<layer<<"\n";
    
    return 0;
}
