#include<bits/stdc++.h>
using namespace std;

struct UnionFind {
    vector<int> data;
    UnionFind(int size) : data(size, -1) {}
    bool unite(int x, int y) {
        x=root(x), y=root(y);
        if (x!=y) {
            if (data[y]<data[x]) {
                swap(x, y);
            }
            data[x]+=data[y], data[y]=x;
        }
        return x!=y;
    }

    bool find(int x, int y) {
        return root(x)==root(y);
    }

    int root(int x) {
        return data[x]<0 ? x : data[x]=root(data[x]);
    }

    int size(int x) {
        return -data[root(x)];
    }
};


int main(){
    int n,q,ans=0;
    scanf("%d %d",&n,&q);
    UnionFind uf(n);
    for (int i=0;i<q;i++) {
        int a,b;
        scanf("%d %d",&a,&b);
        uf.unite(a-1,b-1);
    }
    set<int> s;
    for (int i=0;i<n;i++) {
        s.insert(uf.root(i));

    }
    printf("%ld\n",s.size()-1);
    return 0;
}