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
    int n,m,ans=0,cnt=1;
    sc1(n);
    vector <int> p(n);
    vector <int> q(n);
    vector <int> w(n);
    rep(i,n) sc1(p.at(i));
    rep(i,n) sc1(q.at(i));
    rep(i,n) w.at(i)=i+1;
    do{
        bool fx=1;
        bool fy=1;
        rep(i,n) {
            if (w.at(i)!=p.at(i)) fx=0;
            if (w.at(i)!=q.at(i)) fy=0;

        }
        if(fx) ans-=cnt;
        if(fy) ans+=cnt;
        cnt++;
    } while (next_permutation(w.begin(),w.end()));
    cout << abs(ans) << endl;
    return 0;
}
