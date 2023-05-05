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
    int r,c,k,n,m,x,y,cnt=0,ans=0;
    cin >> r >> c >> k >> n;
    if (n>50 || r>50 || c>50) {print(-1); return 0;}
    map<int,int> wr;
    map<int,int> wc;
    map<int,int> rr;
    map<int,int> cc;
    //vector<vector<bool>> ww(1e5+2,vector<bool>(1e5+2,0));
    vector<int> a(n);
    //vector<vector<int>> w(r+3,vector<int>(c+3,0));
    rep(i,n) {
        cin >> y >> x;
        rr[y]++;
        cc[x]++;
        //ww.at(y).at(x)=1;
    }
    for(int i=1;i<=r;i++) wr[rr[i]]++; 
    for(int i=1;i<=c;i++) wr[cc[i]]++; 
    rep(i,k+1){
        int t=wr[i];
        cout << t << endl;
    }

    print(1e5+5);
    //print(ans);
    return 0;
}
