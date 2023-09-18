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

int main(){//TLE WA
    int mod=1e9+7;
    int n,h,w,k,nx,ny,wx,wy,x1,y1,x2,y2,z,cnt=0,ans=0;
    cin >> h >> w;
    cin >> x1 >> y1;
    cin >> x2 >> y2;
    //x2--; y2--;
    string s,t;
    vector<string> a(h);
    vector<vector<pair<int,int>>> p(h,vector<pair<int,int>>(w,{mod,mod}));
    rep(i,h) cin >> a.at(i);
    p.at(x1-1).at(y1-1)={0,0};

    vector<int> xx={0,0,1,-1};//4
    vector<int> yy={1,-1,0,0};
    vector<int> xxx={1,-1,1,-1, 0,0,2,-2, 2,2,-2,-2, 1,-1,2,-2, 1,-1,2,-2};//20
    vector<int> yyy={1,-1,-1,1, 2,-2,0,0, -2,2,-2,2, 2,-2,1,-1, -2,2,-1,1};
    
    vector<pair<int,int>> ee;
    vector<pair<int,int>> oo;
    ee.push_back({x1-1,y1-1});
    rep(i,mod){
        if((i%2 && oo.size()==0) || (i%2==0 && ee.size()==0)) break;

        
        if(i%2){
            while(oo.size()){
                nx=oo.back().first;
                ny=oo.back().second;
                oo.pop_back();
                rep(j,4){
                    wx=nx+xx.at(j);
                    wy=ny+yy.at(j);
                    if(wx>=0 && wx<h && wy>=0 && wy<w && a.at(wx).at(wy)=='.'){
                        cnt=p.at(nx).at(ny).second;
                        if(p.at(wx).at(wy).second>cnt){
                            p.at(wx).at(wy)={i,cnt};
                            if(wx!=x2 && wy!=y2) ee.push_back({wx,wy});
                        }
                    }
                }

                rep(j,20){
                    wx=nx+xxx.at(j);
                    wy=ny+yyy.at(j);
                    if(wx>=0 && wx<h && wy>=0 && wy<w && a.at(wx).at(wy)=='.'){
                        cnt=p.at(nx).at(ny).second;
                        if(p.at(wx).at(wy).second>cnt+1){
                            p.at(wx).at(wy)={i,cnt+1};
                            if(wx!=x2 && wy!=y2) ee.push_back({wx,wy});
                        }
                    }
                }
            }
        }else if(i%2==0){
            while(ee.size()){
                nx=ee.back().first;
                ny=ee.back().second;
                ee.pop_back();
                rep(j,4){
                    wx=nx+xx.at(j);
                    wy=ny+yy.at(j);
                    if(wx>=0 && wx<h && wy>=0 && wy<w && a.at(wx).at(wy)=='.'){
                        cnt=p.at(nx).at(ny).second;
                        if(p.at(wx).at(wy).second>cnt){
                            p.at(wx).at(wy)={i,cnt};
                            if(wx!=x2 && wy!=y2) oo.push_back({wx,wy});
                        }
                    }
                }

                rep(j,20){
                    wx=nx+xxx.at(j);
                    wy=ny+yyy.at(j);
                    if(wx>=0 && wx<h && wy>=0 && wy<w && a.at(wx).at(wy)=='.'){
                        cnt=p.at(nx).at(ny).second;
                        if(p.at(wx).at(wy).second>cnt+1){
                            p.at(wx).at(wy)={i,cnt+1};
                            if(wx!=x2 && wy!=y2) oo.push_back({wx,wy});
                        }
                    }
                }
            }
        }

    }

    ans=p.at(x2-1).at(y2-1).second;
    cout << ((ans==mod)?-1:ans) << endl;
    return 0;
}