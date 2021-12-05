#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)

int main(){
    int n,m;
    sc1(n);
    pair<int, int> p={0,0}, q={0,0};
    map<int ,int> a, b;
    rep(i,n){
        sc1(m);
        if(i%2)  a[m]++;
        else b[m]++;
    }
    for(auto x=a.begin();x!=a.end();x++) {
        if (x->second > a[p.first]) {
            p.second=p.first;
            p.first = x->first;
        } else if (x->second > a[p.second]) {
            p.second = x->first;
        }
    }

    for(auto x=b.begin();x!=b.end();x++) {
        if (x->second > b[q.first]) {
            q.second=q.first;
            q.first = x->first;
        } else if (x->second > b[q.second]) {
            q.second = x->first;
        }
    }
    printf("%d\n",p.first!=q.first?(n/2-a[p.first])+(n/2-b[q.first]):min((n/2-a[p.second])+(n/2-b[q.first]), (n/2-a[p.first])+(n/2-b[q.second])));
    return 0;
}
