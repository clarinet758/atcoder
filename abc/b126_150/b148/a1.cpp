#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)


int main(){
    int mod=1000000007;
    int a,b;
    sc1(a);
    sc1(b);
    vector <bool> ans(5);
    ans.at(a)=1;
    ans.at(b)=1;
    for(int i=1;i<4;i++) {
        if (ans.at(i)==0) printf("%d\n",i);
    }
    return 0;
}
