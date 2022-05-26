#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)

int main(){
    vector <int> a(5);
    rep(i,3)  sc1(a[i]);
    sort(a.rbegin(),a.rend());
    printf("%d\n",a[0]*10+a[1]+a[2]);
    return 0;
}
