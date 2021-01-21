#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)
#define sc2(a,b)  scanf("%d %d",&a,&b)

int main(){
    int n,k,ans=1e9+7;
    map <int,int> w;
    priority_queue<int> lq,rq;
    sc2(n,k);
    rep(i,n) {
        int h;
        sc1(h);
        if (w[h]==0)  rq.push(-h);
        w[h]++;
    }

    int l=0,r=0,s=0;
    while(!rq.empty()) {
        s+=w[-1*rq.top()];
        r=-1*rq.top();
        lq.push(-1*r);
        rq.pop();
        while(s>=k) {
            l=-1*lq.top();
            if (s>=k) ans=min(ans,r-l);
            s-=w[l];
            lq.pop();
        }
    }
    printf("%d\n",ans);
    return 0;
}
