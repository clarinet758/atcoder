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
double hen(int x1, int y1, int x2, int y2) {
    double z;
    if(x1==x2) z=abs(y1-y2);
    else if(y1==y2) z=abs(x1-x2);
    else z=pow((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2),0.5);
    return z;
}

int main(){
    int mod=1000000007;
    int x1,x2,x3,y1,y2,y3,n,m,cnt=0,ans=0;
    cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;
    double x=hen(x1,y1,x2,y2);
    double y=hen(x3,y3,x2,y2);
    double z=hen(x1,y1,x3,y3);
    //cout << x << y << z << endl;
    double p=(x+y+z)/2.0;
    //cin >> m;
    //sort(a.begin(),a.end());
    //scanf("%d %d",&n,&m);

    printf("%.10lf\n",(pow((p*(p-x)*(p-y)*(p-z)),0.5)));
    return 0;
}
