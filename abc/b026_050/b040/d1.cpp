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
void yneso(int a) {if(a) Yes; else No;}

//int64_t はatcoderメリット不明のため long long
typedef long long ll;
//#define ll int64_t

//
int souwa(int a) {return (1+a)*a/2;}
int lcm(int a,int b) { return a*b/__gcd(a,b); }
//l l lcm(ll a,ll b) { return a*b/__gcd(a,b); }

//
double tilt(int x1,int y1,int x2,int y2) {return (1.0*y2-1.0*y1)/(1.0*x2-1.0*x1);}
double tri(int xa,int ya,int xb,int yb,int xc,int yc) {return (1.0*xa-1.0*xc)*(1.0*yb-1.0*yc)-(1.0*xb-1.0*xc)*(1.0*ya-1.0*yc);}
bool sankaku(int a,int b,int c) {vector <int> t={a,b,c};sort(t.begin(),t.end()); return t.at(0)+t.at(1)>t.at(2);};

/** sort(ar.begin(),ar.end())
 * vector<vector<int>> a(5,vector<int>)
    int sum=accumulate(ar.begin(),ar.end(),0); 
    do {// do内部で作られた順列に対して必要な処理を行う
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
    int n,m,q,k;
    cin >> n >> m;
    UnionFind uf(n+1);

    vector<vector<int>> w(m, vector<int> (3,0));
    rep(i,m)  cin >> w.at(i).at(1) >> w.at(i).at(2) >> w.at(i).at(0); 

    cin >> q;
    vector<vector<int>> u(q,vector<int>(3,0));
    rep(i,q) {
        cin >> u.at(i).at(1) >> u.at(i).at(0);
        u.at(i).at(2)=i;
    }
    sort(w.begin(),w.end());
    sort(u.begin(),u.end());
    vector<int> ans(q);
    k=m-1;
    
    for(int i=q-1;i>=0;i--){
        for(int j=k;j>=0;j--){
            k=j;
            if(u.at(i).at(0)>=w.at(j).at(0)) break;
            uf.unite(w.at(j).at(1),w.at(j).at(2));
        }
        ans.at(u.at(i).at(2))=uf.size(u.at(i).at(1));
    }
    rep(i,q) cout << ans.at(i) << endl;
    return 0;
}
