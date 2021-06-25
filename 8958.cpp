//
//  8958.cpp
//  BOJ
//
//  Created by 유수안 on 2021/06/24.
//

#include <iostream>
#include <string>
using namespace std;

int main()
{
    int n;
    string arr;
    
    cin>>n;
    for(int i=0; i<n; i++)
    {
        cin>>arr;
        int sum, cnt;
        sum=0;
        cnt=0;
        for(int j=0; j<arr.length(); j++){
            if(arr[j]=='O') cnt++;
            else cnt=0;
            sum += cnt;
        }
        cout<<sum<<"\n";
    }

}
