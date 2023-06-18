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
    int n,m,x,y,q,cnt=0,ans=0;
    string s,t;
    cin >> n;
    vector<vector<int>> w(n,vector<int>());
    rep(i,n-1) {
        cin >> x >> y;
        x--; y--;
        w.at(x).push_back(y);
        w.at(y).push_back(x);
    }
    vector<int> p(n,0);
    vector<int> h;
    cin >> q;
    if (q>1) return 0;
    cin >> x >> y;
    x--; y--;
    h.push_back(x);
    for(;;) {
        m=h.at(h.size()-1);
        h.pop_back();
        rep(i,w.at(m).size()) {
            int j=w.at(m).at(i);
            if (p.at(j)==0) {
                h.push_back(j);
                p.at(j)=p.at(m)+1;
            }
        }
        if(p.at(y)>0) {
            cout << p.at(y)+1 << endl;
            return 0;
        }
    }
    return 0;
}