#include<bits/stdc++.h>
using namespace std;

#define ll int64_t
#define rep(i,n)  for(int i=0;i<n;++i)
#define per(i,n)  for(int i=n-1;i>=0;--i)
#define ii1(a)  scanf("%d",&a)
#define ii2(a,b)  scanf("%d %d",&a,&b)
#define ii3(a,b,c)  scanf("%d %d %d",&a,&b,&c)
#define ll1(a)  scanf("%lld",&a)
#define ll2(a,b)  scanf("%lld %lld",&a,&b)
#define ll3(a,b,c)  scanf("%lld %lld %lld",&a,&b,&c)
#define PI 3.1415926535897932

void ww(int n,vector<int> &a) { rep(i,n) ii1(a.at(i)); }

//
int souwa(int a) {return (1+a)*a/2;}
int lcm(int a,int b) { return a*b/__gcd(a,b); }
//long long lcm(ll a,ll b) { return a*b/__gcd(a,b); }

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
    int a,b,c,x,y,n,m,ans;
    cin >> a >> b >> c >> x >> y;
    ans=c*max(x,y)*2;
    if (x>y) {
        int p=(x-y)*2*c;
        int t=(x-y)*a;
        //cout << p << " " << t << endl;
        if (p>t) ans=ans-p+t;
    }
    if (x<y) {
        int p=(y-x)*2*c;
        int t=(y-x)*b;
        if (p>t) ans=ans-p+t;
    }
    if (a+b<c*2) {
        ans-=min(x,y)*2*c;
        ans+=min(x,y)*a+min(x,y)*b;
    }
    cout << ans << endl;


    return 0;
}
