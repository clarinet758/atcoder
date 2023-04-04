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
    int n,m=0,x=0,y=0,cnt=0;
    cin >> n;
    if (n>8) {
        cout << 0 << endl;
        return 0;
    }
    vector<int> a(n);
    vector<int> b(n);
    rep(i,n) cin >> a.at(i);
    rep(i,n) b.at(i)=i;
    vector<vector<int>> h;
    do {
        //for (int q=0;q<h.size();q++) {
            //m=1;
            //for(int qq=0;qq<n;qq++) {
            //    if(h.at(q).at(qq)!=a.at(qq)) m=0;
            //}
            //if(m) break;
        //}
        //if(m) continue;
        //else h.push_back(a);
        cnt++;
        //cout << a.at(0) << a.at(1)  << endl;
        for(int i=1;i<n;i++) {
            y=0;
            for(int j=i-1;j>=0;j--) if(a.at(b.at(i))%a.at(b.at(j))==0) y++;
            if(y%2==0) x++;
        }
    } while (next_permutation(b.begin(),b.end()));
    x+=cnt;

    //sort(a.begin(),a.end());
    //scanf("%d %d",&n,&m);
    //cout << h.size() << endl;
    //cout << cnt << endl;
    printf("%.10lf\n",1.0*x/cnt);

    return 0;
}
