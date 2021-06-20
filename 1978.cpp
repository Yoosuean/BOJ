//
//  1978.cpp
//  BOJ
//
//  Created by 유수안 on 2021/06/14.
//


#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;

    int arr[100];
    int cnt = N;
    int max = 0; //최댓값
    for(int i=0; i<N; i++){
        cin >> arr[i];
        if(arr[i] > max)
            max = arr[i];
        // 1 제외
        if(arr[i] == 1) cnt--;
    }

    for(int i=2; i<max; i++){
        for(int j=0; j<N; j++){
            if(arr[j] != 0 && ((arr[j]!=i) && ((arr[j]%i)==0))){
                arr[j] = 0;
                cnt --;
            }
        }
    }
    cout << cnt <<"\n";
    return 0;
}
