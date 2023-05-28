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
#define print(a) cout << a << endl
#define pp puts("")

#define Yes printf("Yes\n")
#define No printf("No\n")
void yneso(int a) {if(a) Yes; else No;}

//int64_t はatcoderメリット不明のため long long
typedef long long ll;
//#define ll int64_t

//
int souwa(int a) {return (1+a)*a/2;}
int lcm(int a,int b) { return a*b/__gcd(a,b); }
//l l lcm(ll a,ll b) { return a*b/__gcd(a,b); }

//
double tilt(int x1,int y1,int x2,int y2) {return (1.0*y2-1.0*y1)/(1.0*x2-1.0*x1);}
double tri(int xa,int ya,int xb,int yb,int xc,int yc) {return (1.0*xa-1.0*xc)*(1.0*yb-1.0*yc)-(1.0*xb-1.0*xc)*(1.0*ya-1.0*yc);}
bool sankaku(int a,int b,int c) {vector <int> t={a,b,c};sort(t.begin(),t.end()); return t.at(0)+t.at(1)>t.at(2);};

/** sort(ar.begin(),ar.end())
 * vector<vector<int>> a(5,vector<int>)
    int sum=accumulate(ar.begin(),ar.end(),0); 
    do {// do内部で作られた順列に対して必要な処理を行う
        // cout << w.at(0) << w.at(1) << w.at(2) << endl;
    } while (next_permutation(w.begin(),w.end()));  //ex. vector <int> w= {1,2,3}; **/

// 何か貼るときはココから下
vector< bool > prime_table(int n) {
  vector< bool > prime(n + 1, true);
  if(n >= 0) prime[0] = false;
  if(n >= 1) prime[1] = false;
  for(int i = 2; i * i <= n; i++) {
    if(!prime[i]) continue;
    for(int j = i * i; j <= n; j += i) {
      prime[j] = false;
    }
  }
  return prime;
}
vector< int > enumerate_primes(int n) {
  if(n <= 1) return {};
  auto d = prime_table(n);
  vector< int > primes;
  primes.reserve(count(begin(d), end(d), true));
  for(int i = 0; i < d.size(); i++) {
    if(d[i]) primes.push_back(i);
  }
  return primes;
}



int main(){
    int mod=1e9+7;
    ll n,k,x,y,z,cnt=1ll,ans=1ll;
    cin >> n;
    vector<int> p=enumerate_primes(1005);
    vector<int> w(1000,0);

    rep(i,n){
      cnt=i+1;
      rep(j,p.size()){
        if(cnt==1) break;
        for(;;) {
          if(cnt%p.at(j)==0) {
            cnt/=p.at(j);
            w.at(j)++;
          }else{
            break;
          }
        }
      }
    }
    rep(i,1000) ans=(ans*(w.at(i)+1))%mod;
    print(ans);
    return 0;
}
