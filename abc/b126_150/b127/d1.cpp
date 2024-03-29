#include<bits/stdc++.h>
//#include<stdbool.h>
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

int main(){//小さい方から適当にはだめっぽい。後で考える。
    int mod=1e9+7;
    int a,b,c,n,m,k,x,y=0,z,cnt=0;
    ll ans=0ll;
    cin >> n >> m;
    priority_queue<int, vector<int>, greater<int>> q;
    map<int, int>w;
    vector<pair <int,int>> p(m);
    rep(i,n){
        cin >> x;
        w[x]++;
        if(w[x]==1) q.push(x);
    }
    rep(i,m) {
        cin >> p.at(i).second >> p.at(i).first;
    }
    sort(p.begin(),p.end());
    rep(i,m){
        y=p.at(i).first;
        x=p.at(i).second;
        rep(j,mod){
            z=q.top();
            if(z<y){
                q.pop();
                if(w[y]==0) q.push(y);
                w[y]+=min(w[z],x);
                if(x>=w[z]) {x-=w[z]; w[z]=0;}
                else {w[z]-=x; x=0; q.push(z);}
            }else{
                break;
            }
            if(x==0) break;
        }
    }
    rep(i,n){
        x=q.top();
        q.pop();
        ans+=1ll*w[x]*x;
        if(q.empty()) break;
    }
    cout << ans << endl;
    return 0;
}