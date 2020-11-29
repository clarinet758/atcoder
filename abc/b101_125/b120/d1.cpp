#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc2(a,b)  scanf("%d %d",&a,&b)

struct UnionFind {
    vector<int> data;
    UnionFind(int size) : data(size, -1) {}
    bool unite(int x, int y) {
        x=root(x), y=root(y);
        if (x!=y) {
            if (data[y]<data[x])  swap(x, y); 
            data[x]+=data[y], data[y]=x;
        }
        return x!=y;
    }

    bool find(int x, int y)  { return root(x)==root(y); }

    int root(int x)  { return data[x]<0 ? x : data[x]=root(data[x]); }

    int size(int x)  { return -data[root(x)]; }
};

long long ans[100005];

int main(){
    long long  n,m;
    scanf("%lld %lld",&n,&m);
    vector <pair<int,int>> w(m);
    UnionFind uf(n);
    for (int i=0;i<m;i++) {
        int a,b;
        sc2(a,b);
        w[i].first=a-1;
        w[i].second=b-1;
    }
    ans[m-1]=n*(n-1)/2;
    for(int i=m-1;i>0;i--) {
        ans[i-1]=ans[i];
        if (uf.find(w[i].first,w[i].second)==false) {
            ans[i-1]-=(long long)uf.size(w[i].first)*uf.size(w[i].second);
            uf.unite(w[i].first,w[i].second);
        }
    }
    rep(i,m) printf("%lld\n",ans[i]);
    return 0;
}
