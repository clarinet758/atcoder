#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)

int main(){
    int n,a;
    sc1(n);
    bool f=1;
    rep(i,n) {
        sc1(a);
        if ((a%2==0) && ((a%3==0) || (a%5==0))) f=f;
        else if (a%2==0) f=0;
    }
    printf("%s\n",f?"APPROVED":"DENIED");
    return 0;
}
