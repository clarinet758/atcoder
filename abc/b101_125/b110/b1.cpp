#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)


int main(){
    int n,m,x,y;
    scanf("%d %d %d %d",&n,&m,&x,&y);
    vector <int> a(n),b(m);
    rep(i,n) sc1(a[i]);
    rep(i,m) sc1(b[i]);
    sort(a.rbegin(),a.rend());
    sort(b.begin(),b.end());
    for(int i=x+1;i<=y;i++) {
        if (i>a[0] && i<=b[0]) {
            printf("No War\n");
            return 0;
        }
    }
    printf("War\n");
    return 0;
}
