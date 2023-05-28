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

// 何か貼るときはココから下に


int main(){
    int mod=1e9+7;
    int n,a,b,e=0,z;
    ll k,x=1ll,y=1ll,cnt=0ll,ans=0ll,t=0ll;
    cin >> n >> a >> b;
    vector<ll> v;
    vector<vector<ll>> p(51,vector<ll>(51,0));
    for(int i=0;i<51;i++){
        p.at(i).at(0)=1;
        p.at(i).at(i)=1;
    }
    for(int i=1;i<51;i++){
        for(int j=1;j<=i;j++){
            p.at(i).at(j)=p.at(i-1).at(j-1)+p.at(i-1).at(j);
        }
    }

    map<ll,int> w;
    rep(i,n) {
        cin >> k;
        w[k]++;
        if(w[k]==1) v.push_back(k);
    }
    sort(v.begin(),v.end());

    z=v.size()-1;
    if(z==0 ||a<=w[v.back()]){
        for(int i=a;i<=b;i++) ans+=p.at(w[v.at(z)]).at(i); 
        printf("%.10lf\n",v.at(z)*1.0);
        cout << ans << endl;
        return 0;
    }

    for(int i=v.size()-1;i>=0;i--){
        if(a>e+w[v.at(i)]){
            cnt+=v.at(i)*w[v.at(i)];
            e+=w[v.at(i)];
        }else{
            cnt+=v.at(i)*(a-e);
            printf("%.10lf\n",(cnt*1.0)/a);
            //cout << w[v.at(i)] << endl;
            cout << p.at(w[v.at(i)]).at(a-e) << endl;
            return 0;
        }
    }
    return 0;
}