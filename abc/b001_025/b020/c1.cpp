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
//int64_t はatcoderメリット不明のため long long
#define ll long long
//#define ll int64_t
#define print(a) cout << a << endl


//
int souwa(int a) {return (1+a)*a/2;}
int lcm(int a,int b) { return a*b/__gcd(a,b); }
//l l lcm(ll a,ll b) { return a*b/__gcd(a,b); }

//
bool sankaku(int a,int b,int c) {vector <int> t={a,b,c};sort(t.begin(),t.end()); return t.at(0)+t.at(1)>t.at(2);};

/** sort(ar.begin(),ar.end())
    int sum=accumulate(ar.begin(),ar.end(),0); 
    do {// do内部で作られた順列に対して必要な処理を行う
        // cout << w.at(0) << w.at(1) << w.at(2) << endl;
    } while (next_permutation(w.begin(),w.end()));  //ex. vector <int> w= {1,2,3}; **/

// 何か貼るときはココから下に

int main(){
    int mod=1000000007;
    int h,w,t,sx,sy,gx,gy,cnt=0,ans=0;
    string s;
    cin >> h >> w >> t;
    vector<string> d(h);
    rep(i,h) {
        cin >> d.at(i);
        rep(j,w) {
            if (d.at(i).at(j)=='S') {sx=j; sy=i;}
            if (d.at(i).at(j)=='G') {gx=j; gy=i;}
        }
    }
    //cout << d.at(0).at(1) << endl;
    //cout << d.at(1).at(1) << endl;
    int l=-1,r=t+1;
    //string p=d.back();
    //string p=d.at(0);
    //cout << p << endl;
    for(;;) {
        if (r-l<=1) break;
        vector<pair<int,int>> dd;
        vector<vector<int>> m(h,vector<int>(w,t+5));
        dd.push_back({sy,sx});
        m.at(sy).at(sx)=0;
        cnt=(l+r)/2;
        for(;;){
            if (dd.empty()) break;
            int y=dd.back().first, x=dd.back().second,p;
            dd.pop_back();
            if(x-1>=0) {
                if (d.at(y).at(x-1)=='#') p=cnt;
                else p=1;
                if (m.at(y).at(x-1)>m.at(y).at(x)+p) {
                    if(x-1!=gx || y!=gy) dd.push_back({y,x-1});
                    m.at(y).at(x-1)=m.at(y).at(x)+p;
                }
            }
            if(y-1>=0) {
                if (d.at(y-1).at(x)=='#') p=cnt;
                else p=1;
                if (m.at(y-1).at(x)>m.at(y).at(x)+p) {
                    if(x!=gx || y-1!=gy) dd.push_back({y-1,x});
                    m.at(y-1).at(x)=m.at(y).at(x)+p;
                }
            }
            if(y+1<h) {
                if (d.at(y+1).at(x)=='#') p=cnt;
                else p=1;
                if (m.at(y+1).at(x)>m.at(y).at(x)+p) {
                    if(x!=gx || y+1!=gy) dd.push_back({y+1,x});
                    m.at(y+1).at(x)=m.at(y).at(x)+p;
                }
            }
            if(x+1<w) {
                if (d.at(y).at(x+1)=='#') p=cnt;
                else p=1;
                if (m.at(y).at(x+1)>m.at(y).at(x)+p) {
                    if(x+1!=gx || y!=gy) dd.push_back({y,x+1});
                    m.at(y).at(x+1)=m.at(y).at(x)+p;
                }
            }
        }
        if (m.at(gy).at(gx)<=t) l=cnt;
        else r=cnt;
    }
    print(l);
    return 0;
}