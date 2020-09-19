#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)
#define sc2(a,b)  scanf("%d %d",&a,&b)
#define sl1(a)  scanf("%lld",&a)
#define sl2(a,b)  scanf("%lld %lld",&a,&b)


long long d[200002];
int w[200002];
int main(){
    long long mod=998244353;
    set<int> u;
    
    int n,k;
    sc2(n,k);
    for(int i=0;i<k;i++) {
        int a,b;
        sc2(a,b);
        w[a]+=1;
        w[b]=-1;
        //for (int j=a;j<=b;j++) u.insert(j);
    }
    d[0]=1;
    for (int i=0;i<n-1;i++){
        if (d[i]==0) continue;
        //for(auto itr=u.begin();itr!=u.end();++itr){
        bool f=0;
        for (int j=1;j<n;j++) {
            if (w[j]==1) f=1;
            //int j=*itr;
            if (i+j<=n && f) {
                d[i+j]+=d[i];
                d[i+j]%=mod;
            }
            if (w[j]==-1) f=0;
        }
    }
    printf("%lld\n",d[n-1]);
    return 0;
}

//printf("%lld %lld\n",d[n],d[n-1]);
//for (int i=0;i<5;i++) printf("%d\n",w[i]);
