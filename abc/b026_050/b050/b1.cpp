#include<bits/stdc++.h>

using namespace std;

#define PI 3.1415926535897932

int main(){
    int mod=1000000007;
    int n,m,chk,p,x;
    scanf("%d",&n);
    vector<int> t(n);
    for (auto&e:t) {
        scanf("%d",&e);
    }
    chk = accumulate(t.begin(),t.end(),0);
    scanf("%d",&m);
    for (int i=0;i<m;i++) {
        scanf("%d %d",&p,&x);
        printf("%d\n",chk-(t[p-1]-x));
    }
    return 0;
}
