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

int main(){
    int mod=1e9+7;
    int h,w,n,k,x,y,z,cnt=0,ans=0;
    cin >> h >> w;
    vector<vector<int>> c(10,vector<int>(10,0));

    rep(i,10)rep(j,10) cin >> c.at(i).at(j);
    
    vector<int> ww(10,mod);

    rep(i,10){
        vector<int> e={i};
        vector<int> o;
        vector<int> p(10,mod);
        p.at(i)=0;

        rep(j,111){
            for(;;){
                if(j%2 && o.size()==0) break;
                else if(j%2==0 && e.size()==0) break;
                if(j%2) {x=o.back(); o.pop_back();}
                else {x=e.back(); e.pop_back();}

                rep(k,10){
                    if(c.at(x).at(k)+p.at(x)<p.at(k)){
                        p.at(k)=c.at(x).at(k)+p.at(x);
                        if(j%2) e.push_back(k);
                        else o.push_back(k);
                    }
                }
            }

        }
        ww.at(i)=p.at(1);
    }
    rep(i,h*w){
        cin >> y;
        if (y!=-1)ans+=ww.at(y);
    }
    cout << ans << endl;

    return 0;
}