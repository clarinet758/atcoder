#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc2(a,b)  scanf("%d %d",&a,&b)

int main(){
    int a,b,x;
    sc2(a,b);
    x=b*10;
    rep(i,1000) {
        if ((x+i)/10==b && (x+i)*8/100==a) {
            cout << x+i << endl;
            return 0;
        } else  if ((x-i)/10==b && (x-i)*8/100==a) {
            cout << x-i << endl;
            return 0;
        }

    }
    printf("-1\n");
    return 0;
}