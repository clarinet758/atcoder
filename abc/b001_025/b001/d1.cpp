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
    int n,m,x,y,cnt=0,ans=0;
    cin >> n;
    vector<vector<int>> a(25,vector<int>(61));
    rep(i,25) rep(j,61) a.at(i).at(j)=0;
    rep(i,n){
        scanf("%d-%d",&x,&y);
        a.at(x/100).at(x%100/10*10+((x%10<5)?0:5))++;
        if(y%10>5) y=y-y%10+10;
        else if(y%10==5) true;
        else if(y%10>0) y=y-y%10+5;
        if (y%100==60) y+=40;
        a.at(y/100).at(y%100)--;
    }
    rep(i,25) rep(j,60) {
        if(a.at(i).at(j)>0 && cnt==0) {
            printf("%02d%02d-",i,j);
        } else if(a.at(i).at(j)==cnt*-1 && cnt>0) {
            printf("%02d%02d\n",i,j);
        }
        cnt+=a.at(i).at(j);
    }

    return 0;
}