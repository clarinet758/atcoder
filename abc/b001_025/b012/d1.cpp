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

vector<vector<int>> w;
void wf(int n){
    rep(i,n) rep(j,n) rep(k,n){
        w.at(j).at(k)=min(w.at(j).at(k),w.at(j).at(i)+w.at(i).at(k));

    }
}



int main(){
    int mod=1000000007;
    int n,m,a,b,t,x,cnt=0,ans=0;
    cin >> n >> m;
    w=vector<vector<int>> (n+1,vector<int>(n+1,mod));
    rep(i,n) w.at(i).at(i)=0;
    rep(i,m) {
        cin >> a >> b >> t;
        w.at(a).at(b)=t;
        w.at(b).at(a)=t;
    }
    cnt=mod;
    wf(n+1);
    //cout << w.at(1).at(1) << w.at(1).at(2) << w.at(1).at(3) << endl;
    //cout << w.at(2).at(1) << w.at(2).at(2) << w.at(2).at(3) << endl;
    //cout << w.at(3).at(1) << w.at(3).at(2) << w.at(3).at(3) << endl;
    rep(i,n) {
        sort(w.at(i+1).begin(),w.at(i+1).end());
        x=w.at(i+1).at(n-1);
        if(x<cnt) {
            cnt=x;
        }
    }
    print(cnt);
    return 0;
}
