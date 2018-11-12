#include<bits/stdc++.h>
using namespace std;

// WAAAAAAAAAAAAAA

int main(){
    int n,a,b;
    scanf("%d %d %d",&n,&a,&b);
    vector<int> s(n);
    for (auto&e:s) scanf("%d",&e);
    int t = accumulate(s.begin(),s.end(),0);
    sort(s.begin(),s.end());
    if (s[0]==s[n-1]) {
        printf("-1\n");
    } else {
        double p=1.0*b/(s[n-1]-s[0]);
        double q=a-p*(1.0*t/n);
        printf("%.8f %.8f\n",p,q);
    }
    return 0;
}
