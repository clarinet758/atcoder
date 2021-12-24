#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)

int main(){
    int n,m,a;
    sc1(n);
    vector <int> w(n);
    rep(i,n-1) {
        sc1(a);
        w.at(a-1)++;
    }
    rep(i,n-1) printf("%d\n",w.at(i));
    printf("0\n");
    return 0;
}
