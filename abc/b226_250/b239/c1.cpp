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
    int x1,y1,x2,y2,ans=0;
    cin >> x1 >> y1 >> x2 >> y2;
    vector<pair<int,int>> a(16);
    a.at(0).first=x1+1; a.at(0).second=y1+2;
    a.at(1).first=x2+1; a.at(1).second=y2+2;

    a.at(2).first=x1+2; a.at(2).second=y1+1;
    a.at(3).first=x2+2; a.at(3).second=y2+1;

    a.at(4).first=x1+2; a.at(4).second=y1-1;
    a.at(5).first=x2+2; a.at(5).second=y2-1;
    
    a.at(6).first=x1+1; a.at(6).second=y1-2;
    a.at(7).first=x2+1; a.at(7).second=y2-2;

    a.at(8).first=x1-1; a.at(8).second=y1-2;
    a.at(9).first=x2-1; a.at(9).second=y2-2;
    
    a.at(8).first=x1-1; a.at(8).second=y1-2;
    a.at(9).first=x2-1; a.at(9).second=y2-2;

    a.at(10).first=x1-2; a.at(10).second=y1-1;
    a.at(11).first=x2-2; a.at(11).second=y2-1;

    a.at(12).first=x1-2; a.at(12).second=y1+1;
    a.at(13).first=x2-2; a.at(13).second=y2+1;

    a.at(14).first=x1-1; a.at(14).second=y1+2;
    a.at(15).first=x2-1; a.at(15).second=y2+2;

    sort(a.begin(),a.end());
    rep(i,15) if(a.at(i).first==a.at(i+1).first && a.at(i).second==a.at(i+1).second) ans=1;
    cout << ((ans)?"Yes":"No") << endl;
    return 0;
}