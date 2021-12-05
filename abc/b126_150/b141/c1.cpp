#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)
#define sc3(a,b,c)  scanf("%d %d %d",&a,&b,&c)

int main(){
    int mod=1000000007;
    int n,k,q;
    sc3(n,k,q);
    vector <int> res(n,k-q);
    rep(i,q) {
        int a;
        sc1(a);
        res.at(a-1)++;
    }
    rep(i,n) {
        if (res.at(i)>0) {
            cout << "Yes" << endl;
        } else {
            cout << "No" << endl;
        }
    }
    return 0;
}