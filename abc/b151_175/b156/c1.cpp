#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)
#define sc2(a,b)  scanf("%d %d",&a,&b)
#define sc3(a,b,c)  scanf("%d %d %d",&a,&b,&c)


int main(){
    int mod=1000000007;
    int n,m;
    sc1(n);
    vector <int> x(n);
    rep(i,n) sc1(x.at(i));
    int sum=accumulate(x.begin(),x.end(),0);
    int v=sum/n,a=0,b=0;
    rep(i,n){
        a+=(x.at(i)-v)* (x.at(i)-v);
        b+=(x.at(i)-(v+1))* (x.at(i)-(v+1));

    }
    printf("%d\n",min(a,b));
    return 0;
}
