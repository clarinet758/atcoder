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
    int n,q,p,x,y,cnt=0,ans=0;
    string s,t;
    cin >> n;
    vector<vector<int>> d(n,vector<int>(n));
    rep(i,n) rep(j,n) cin >> d.at(i).at(j);
    vector<vector<int>> w(n+1, vector<int>(n+1,0));

    rep(i,n) rep(j,n) w.at(i+1).at(j+1)=w.at(i).at(j+1)+w.at(i+1).at(j)+d.at(i).at(j)-w.at(i).at(j);
    //rep(i,n) rep(j,n) cout << w.at(i+1).at(j+1) << endl;
    vector<int> m(2501,0);
    rep(i,n) rep(j,n) rep(k,n-i) rep(l,n-j) {
        x=w.at(i+k+1).at(j+l+1)+w.at(i).at(j)-w.at(i+k+1).at(j)-w.at(i).at(j+l+1);
        m.at((k+1)*(l+1))=max(m.at((k+1)*(l+1)),x);
    }
    rep(i,2500) m.at(i)=max(m.at(i),m.at(i-1));

    cin >> q;
    rep(i,q) {
        cin >> p;
        cout << m.at(p) << endl;
    }

    //print(y/x);
    return 0;
}
