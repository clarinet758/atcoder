#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)

int main(){
    int d;
    sc1(d);
    printf("Christmas");
    rep(i,25-d) printf(" Eve");
    puts("");
    return 0;
}
