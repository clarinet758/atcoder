#include<bits/stdc++.h>
using namespace std;

#define PI 3.1415926535897932

int lcm(int a,int b) { return a*b/__gcd(a,b); }

class UnionFind {
public:
    vector<int> parent;
    UnionFind(int n) {
        parent=vector<int>(n,-1);
    }

    int root(int a) {
        if (parent[a]<0) return a;
        return parent[a] = root(parent[a]);
    }

    int size(int a) {
        return -parent[root(a)];
    }

    bool con(int a, int b) {
        a=root(a);
        b=root(b);
        if (a==b) return false;
        if (size(a)<size(b)) swap(a,b);
        parent[a]+=parent[b];
        parent[b]=a;
        return true;
    }
};

int main(){
    int mod=1000000007;
    int n,q,p,a,b;
    scanf("%d %d",&n,&q);
    UnionFind uf(n);
    for (int i=0;i<q;i++) {
        scanf("%d %d %d",&p,&a,&b);
        if (p==0) {
            uf.con(a,b);
        } else {
            a=uf.root(a);
            b=uf.root(b);
            printf("%s\n",a==b?"Yes":"No");
        }
    }
    return 0;
}
