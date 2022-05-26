#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)

bool x[200005],y[200005];

int main(){
    int n,o=0,p=0;
    sc1(n);
    vector <int> l(n+5);
    rep(i,n) {
        sc1(l.at(i));
        if (l.at(i)>o) {
            p=o;
            o=l.at(i);
        } else if (l.at(i)>p) {
            p=l.at(i);
        }

        if(x[l.at(i)]==0) {
            x[l.at(i)]=1;
        } else {
            y[l.at(i)]=1;
        }
    } 
    rep(i,n) {
        if (l.at(i)==o && y[o]==1) {
            printf("%d\n",o);
        } else if (l.at(i)==o) {
            printf("%d\n",p);
        } else {
            //printf("%d %d 99 \n",o,l.at(i));
            printf("%d\n",o);
        }
    }
    return 0;
}
