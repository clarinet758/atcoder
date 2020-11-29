#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)

int main(){
    int n,m;
    sc1(n);
    vector <int> l(n);
    rep(i,n) sc1(l[i]);
    sort(l.begin(),l.end());
    int t=accumulate(l.begin(),l.end(),0); 
    printf("%s\n",t-l[n-1]>l[n-1]?"Yes":"No");
    return 0;
}
