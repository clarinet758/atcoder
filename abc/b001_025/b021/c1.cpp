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
    int n,m,x,y,a,b,f=0,cnt=0,ans=0;
    cin >> n;
    cin >> x >> y;

    cin >> m;
    vector<vector<bool>> w(n+3,vector<bool> (n+3,0));
    rep(i,m) {
        cin >> a >> b;
        w.at(a).at(b)=1;
        w.at(b).at(a)=1;
    }

    vector<pair<int,int>> mp(n+3,{mod,1});
    vector<bool> l(n+3,0);
    vector<bool> r(n+3,0);
    l.at(x)=1;
    mp.at(x).first=0;
    mp.at(x).second=1;
    for(;;) {
        if (l.at(y)==1 || r.at(y)==1) break;
        if (f%2) {
            for(int i=1;i<=n;i++){
                if(r.at(i)){
                    for (int j=1;j<=n;j++) {
                        if (w.at(i).at(j)) {
                            if(mp.at(j).first>mp.at(i).first+1) {
                                mp.at(j).first=mp.at(i).first+1;
                                mp.at(j).second=mp.at(i).second;
                                l.at(j)=1;
                            } else if (mp.at(j).first==mp.at(i).first+1) {
                                mp.at(j).second=(mp.at(j).second+mp.at(i).second)%mod;
                                l.at(j)=1;
                            }
                        }
                    }
                }
                r.at(i)=0;
            }
        } else  {
            for(int i=1;i<=n;i++){
                if(l.at(i)){
                    for (int j=1;j<=n;j++) {
                        if (w.at(i).at(j)) {
                            if(mp.at(j).first>mp.at(i).first+1) {
                                mp.at(j).first=mp.at(i).first+1;
                                mp.at(j).second=mp.at(i).second;
                                r.at(j)=1;
                            } else if (mp.at(j).first==mp.at(i).first+1) {
                                mp.at(j).second=(mp.at(j).second+mp.at(i).second)%mod;
                                r.at(j)=1;
                            }
                        }
                    }
                }
                l.at(i)=0;
            }
        }
        f=(f+1)%2;
    }
    print(mp.at(y).second);
    return 0;
}