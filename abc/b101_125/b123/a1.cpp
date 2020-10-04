#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)

int main(){
    int a[5],k;
    rep(i,5) sc1(a[i]);
    sc1(k);
    int f=1;
    rep(i,5) rep(j,5) if (abs(a[i]-a[j])>k) f=0;
    printf("%s\n",f==1?"Yay!":":(");
    return 0;
}
