#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define per(i,n)  for(int i=n-1;i>=0;--i)
#define sc1(a)  scanf("%d",&a)
#define sc2(a,b)  scanf("%d %d",&a,&b)
#define sc3(a,b,c)  scanf("%d %d %d",&a,&b,&c)
#define sl1(a)  scanf("%lld",&a)
#define sl2(a,b)  scanf("%lld %lld",&a,&b)
#define sl3(a,b,c)  scanf("%lld %lld %lld",&a,&b,&c)
#define PI 3.1415926535897932
#define print(a) cout << a << endl
#define pp puts("")

#define Yes printf("Yes\n")
#define No printf("No\n")
void yneso(int a) {if(a) cout << Yes; else cout << No;}

//int64_t はatcoderメリット不明のため long long
typedef long long ll;
//#define ll int64_t

//
int souwa(int a) {return (1+a)*a/2;}
int lcm(int a,int b) { return a*b/__gcd(a,b); }
ll gcdll(ll a, ll b) { if(b==0ll) return a; else return gcdll(b, a%b); }
ll lcmll(ll a,ll b) { return (a/gcdll(a,b)*b); }
ll maxll(ll a,ll b) {if(a>b){return a;}else{return b;}}
ll minll(ll a,ll b) {if(a<b){return a;}else{return b;}}

double tilt(int x1,int y1,int x2,int y2) {return (1.0*y2-1.0*y1)/(1.0*x2-1.0*x1);}
double tri(int xa,int ya,int xb,int yb,int xc,int yc) {return (1.0*xa-1.0*xc)*(1.0*yb-1.0*yc)-(1.0*xb-1.0*xc)*(1.0*ya-1.0*yc);}
bool sankaku(int a,int b,int c) {vector <int> t={a,b,c};sort(t.begin(),t.end()); return t.at(0)+t.at(1)>t.at(2);};

/** sort(ar.begin(),ar.end())
 * vector<vector<int>> a(5,vector<int>)
    int sum=accumulate(ar.begin(),ar.end(),0); 
    do {// do内部で作られた順列に対して必要な処理を行う
        //必ず事前にソートしておくこと、配列の中身を見ていて？辞書順に次のもの次のもの作成するのでソートしておかないと列挙が漏れる
        // cout << w.at(0) << w.at(1) << w.at(2) << endl;
    } while (next_permutation(w.begin(),w.end()));  //ex. vector <int> w= {1,2,3}; **/

// 何か貼るときはココから下に

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
    int mod=1e9+7;
    int n,m,k,x,y,z,cnt=0,ans=0;
    cin >> n >> m;
    UnionFind uf(n);
    vector<pair<int,int>> a(m);
    vector<ll> w(m+1);
    w.at(m)=1ll*n*(n-1)/2;
    rep(i,m) {
        cin >> x >> y;
        x--;y--;
        a.at(i).first=x;a.at(i).second=y;
    }
    rep(i,m){
        x=a.at(m-1-i).first; y=a.at(m-1-i).second;
        if(uf.find(x,y)) w.at(m-1-i)=w.at(m-i);
        else w.at(m-1-i)=(w.at(m-i)-(uf.size(x)*uf.size(y))); 
        uf.unite(x,y);
    }
    rep(i,m) cout << w.at(i+1) << endl;
    return 0;
}