#include<bits/stdc++.h>
using namespace std;

// https://atcoder.jp/contests/chokudai_S001/submissions/1457913
struct FenwickTree {
    vector<int> v;
    void init(int n) {v.assign(n,int()); }
    void add (int i, int x) { for (;i<(int)v.size();i|=i+1) v[i]+=x; }
    int sum(int i) const {
        int r =int();
        for (--i;i>=0;i=(i&(i+1))-1) r+=v[i];
        return r;
    }
    int sum (int left,int right) const{
        return sum(right)-sum(left);
    }
};

int main(){
    int n;
    scanf("%d",&n);
    vector<int> a(n);
    for (auto&e:a) scanf("%d",&e);
    FenwickTree ft; 
    ft.init(n+1);
    long long ans=0ll;
    for (int i=0;i<n;i++) {
        ans+=i-ft.sum(a[i]);
        ft.add(a[i],1);
    }
    printf("%lld\n",ans);
    return 0;
}
