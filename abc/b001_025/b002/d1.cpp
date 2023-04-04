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
    int n,m,x,y,z,cnt=0,ans=0;

    cin >> n >> m;
    vector<vector<bool>> w(n,vector<bool>(n));
    rep(i,n) rep(j,n) w.at(i).at(j)=(i==j);

    rep(i,m) {
        cin >> x >> y;
        x--; y--;
        w.at(x).at(y)=1;
        w.at(y).at(x)=1;
    }

    for (int i=0;i<(2<<(n-1));i++){
        z=0;
        vector<bool> kouho(n,0);
        rep(j,n) {
            kouho.at(j) = ((i>>j)&1);
            z+=kouho.at(j)-0;
        }
        //cout << kouho.at(4) << kouho.at(3) << kouho.at(2) << kouho.at(1) << kouho.at(0) << endl;
        
        cnt=1;
        rep(j,n) rep(k,n) {
            if (kouho.at(j) && w.at(j).at(k)<kouho.at(k)) cnt=0;
        }
        //cout << cnt << z << endl;
        if (cnt) ans=max(ans,z);
    }

    print(ans);
    return 0;
}
