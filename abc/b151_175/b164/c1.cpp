#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)

int main(){
    int n,ans=0;
    sc1(n);
    map <string, int> w;
    rep(i,n){
        string s;
        cin >>s;
        w[s]++;
    }
    for (auto p:w)  ans++;
    printf("%d\n",ans);
    return 0;
}
