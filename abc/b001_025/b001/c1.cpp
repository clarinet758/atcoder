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
    string s,t;
    cin >> n;
    cin >> m;
    n*=10;
    m=m*10/6;
    if (n>=1125 && n<3375) s="NNE " ;
    else if (n>=3375 && n<5625) s="NE " ;
    else if (n>=5625 && n<7875) s="ENE " ;
    else if (n>=7875 && n<10125) s="E " ;
    else if (n>=10125 && n<12375) s="ESE " ;
    else if (n>=12375 && n<14625) s="SE " ;
    else if (n>=14625 && n<16875) s="SSE " ;
    else if (n>=16875 && n<19125) s="S " ;
    else if (n>=19125 && n<21375) s="SSW " ;
    else if (n>=21375 && n<23625) s="SW " ;
    else if (n>=23625 && n<25875) s="WSW " ;
    else if (n>=25875 && n<28125) s="W " ;
    else if (n>=28125 && n<30375) s="WNW " ;
    else if (n>=30375 && n<32625) s="NW " ;
    else if (n>=32625 && n<34875) s="NNW " ;
    else s="N ";

    if (m<25) m=0;
    else if(m<155) m=1;
    else if(m<335) m=2;
    else if(m<545) m=3;
    else if(m<795) m=4;
    else if(m<1075) m=5;
    else if(m<1385) m=6;
    else if(m<1715) m=7;
    else if(m<2075) m=8;
    else if(m<2445) m=9;
    else if(m<2845) m=10;
    else if(m<3265) m=11;
    else m=12;

    if(m==0) s="C ";
    cout << s << m << endl;

    return 0;
}