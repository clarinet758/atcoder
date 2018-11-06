#include<bits/stdc++.h>
using namespace std;

int main(){
    int n,s,t,tmp=0;
    scanf("%d",&n);
    vector<int> a;
    for (int i=0;i<n;i++) {
        scanf("%d",&s);
        if (s%10==0) tmp+=s;
        else a.push_back(s);
    }
    sort(a.begin(),a.end());
    t=accumulate(a.begin(),a.end(),0);
    if (t%10==0 && t>0) t-=a[0];
    printf("%d\n",(tmp+t)%10==0?0:tmp+t);
    return 0;
}
