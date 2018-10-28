#include<bits/stdc++.h>

using namespace std;

int main(){
    int n,t,c=0,d=0,p,q,ans=0;
    scanf("%d %d",&n,&t);
    vector<int> a(n);
    for (auto&e:a) scanf("%d",&e);
    p=a[0];
    for (int i=1;i<n;i++) {
        p=min(p,a[i]);
        if (a[i]-p==d) {
            c++;
        } else if (a[i]-p>d) {
            c=1;
            d=a[i]-p;
        }
    }
    printf("%d\n",c);
    return 0;
}
