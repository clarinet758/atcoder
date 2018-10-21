#include<bits/stdc++.h>

using namespace std;

#define PI 3.1415926535897932

int main(){
    int n;
    scanf("%d",&n);
    vector<int>ar(n);
    for (auto&e:ar) {
        scanf("%d",&e);
    }
    sort(ar.begin(),ar.end());
    printf("%d\n",ar[n-1]-ar[0]);

    return 0;
}
