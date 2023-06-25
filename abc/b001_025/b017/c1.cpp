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
    int n,m,x,y,cnt=0,ans=0;
    cin >> n >> m;
    if(n>8 || m>8) {cout << -1 << endl; return 0;}
    vector<vector<int>> a(n,vector<int>(3));
    rep(i,n) cin >> a.at(i).at(0) >> a.at(i).at(1) >> a.at(i).at(2);
    rep(i,1<<n){
        vector<int> w(m);
        x=i,cnt=0;
        rep(j,n){
            if(x&1){
                cnt+=a.at(j).at(2);
                for(int k=a.at(j).at(0);k<=a.at(j).at(1);k++) w.at(k-1)=1;
            }
            if(accumulate(w.begin(),w.end(),0)<m) ans=max(ans,cnt);
            x=x>>1;
        }
    }
    print(ans);
    return 0;
}