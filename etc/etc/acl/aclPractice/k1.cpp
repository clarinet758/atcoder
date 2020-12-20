#include<bits/stdc++.h>
#include<atcoder/all>
using namespace std;
using namespace atcoder;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)
#define sc2(a,b)  scanf("%d %d",&a,&b)
#define sc3(a,b,c)  scanf("%d %d %d",&a,&b,&c)
#define PI 3.1415926535897932

using mint = modint998244353;

struct S {
    mint sum, len;
};

struct F {
    mint b,c;
};


S op(S s_l, S s_r) {
    return {s_l.sum + s_r.sum, s_l.len + s_r.len};
}

S e() {
    return {0,0};
}

S mapping(F f,S s) {
    return {f.b * s.sum + f.c * s.len,  s.len};
}

F composition (F f, F g) {
    return {f.b * g.b, f.b * g.c + f.c};
}

F id() {
    return {1,0};
}

int main(){
    int n,q,m,ans;
    sc2(n,q);

    vector<S> v(n);
    rep(i,n) {
        int a; sc1(a);
        v[i]={a,1};
    }

    lazy_segtree<S, op, e, F, mapping, composition, id> seg(v);
    rep(i,q) {
        int t,l,r; sc3(t,l,r);
        if (t==0) {
            int b,c; sc2(b,c);
            seg.apply(l,r, {b,c});
        }
        else printf("%d\n",seg.prod(l,r).sum.val());
    }
    return 0;
}
