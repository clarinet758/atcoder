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
    int n,ans;
    ii1(n);
    
    map<string,vector<int>> x;
    vector<string> w;
    vector<pair<string,int>> t(n);
    rep(i,n){
       string s;
       int p;
       cin >> s >> p;
       x[s].push_back(-p);
       if (x[s].size()==1) w.push_back(s);
       t.at(i).first=s;
       t.at(i).second=-p;
    }
    sort(w.begin(),w.end());
    rep(i,w.size()) sort(x[w.at(i)].begin(),x[w.at(i)].end());
    
    //rep(i,w.size()) cout << w.at(i) << endl;
    //rep(i,n) cout << t.at(i).first << " " << t.at(i).second << endl;
    //rep(i,w.size()) cout << x[w.at(i)].at(0) << endl;

    vector<int> ans2(n);
    rep(i,n) {
        ans=1;
        rep(j,w.size()){
            if (t.at(i).first!=w.at(j)) {
                ans+=x[w.at(j)].size();
            } else {
                break;
            }
        }
        rep(j,x[t.at(i).first].size()) {
            if (t.at(i).second!=x[t.at(i).first].at(j)) ans++;
            else break;
        }
        ans2.at(ans-1)=i+1;
        //cout << ans << endl;
    }
    rep(i,n) cout << ans2.at(i) << endl;
        /**

        **/
    return 0;
}
