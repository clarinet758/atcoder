#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)
#define sc3(a,b,c)  scanf("%d %d %d",&a,&b,&c)

int ww[105][5];
int main(){
    int n,a,b,c;
    sc1(n);
    rep(i,n) {
        sc3(ww[i][0],ww[i][1],ww[i][2]);
        if(ww[i][2]>0) {a=ww[i][0];b=ww[i][1];c=ww[i][2];}
    }

    rep(i,101) rep(j,101) {
        bool f=1;
        int h=c+abs(i-a)+abs(j-b);
        rep (k,n) {
                if (max(0,h-abs(i-ww[k][0])-abs(j-ww[k][1]))!=ww[k][2]) f=0;
        }
        if (f) printf("%d %d %d\n",i,j,h);
    }
    return 0;
}
