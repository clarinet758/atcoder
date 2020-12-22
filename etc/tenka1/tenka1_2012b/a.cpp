#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc3(a,b,c)  scanf("%d %d %d",&a,&b,&c)

int main(){
    int a,b,c;
    sc3(a,b,c);
    rep (i,127) {
        int x=i+1;
        if(x%3==a && x%5==b && x%7==c) printf("%d\n",x);
    }
    return 0;
}
