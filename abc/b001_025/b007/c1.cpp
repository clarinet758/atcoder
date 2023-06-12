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
    int r,c,x1,y1,x2,y2;
    cin >> r >> c;
    cin >> y1 >> x1;
    cin >> y2 >> x2;
    y2--; x2--;
    vector<vector<int>> w(r, vector<int>(c,r*c+100));
    vector<string> b(r);
    vector<pair<int,int>> h;
    rep(i,r) cin >> b.at(i);
    w.at(y1-1).at(x1-1)=0;
    h.push_back({y1-1,x1-1});

    for(;;) {
        if (h.empty()) break;
        int y=h.back().first, x=h.back().second;
        int z=w.at(y).at(x);
        h.pop_back();

        if (y>0 && b.at(y-1).at(x)!='#' && w.at(y-1).at(x)>z+1) { 
            if(y-1!=y2 || x!=x2) h.push_back({y-1,x});
            w.at(y-1).at(x)=z+1;
        }
        if (y<r-1 && b.at(y+1).at(x)!='#' && w.at(y+1).at(x)>z+1) {
            if(y+1!=y2 || x!=x2) h.push_back({y+1,x});
            w.at(y+1).at(x)=z+1;
        }
        if (x<c-1 && b.at(y).at(x+1)!='#' && w.at(y).at(x+1)>z+1) {
            if(y!=y2 || x+1!=x2) h.push_back({y,x+1});
            w.at(y).at(x+1)=z+1;
        }
        if (x>0 && b.at(y).at(x-1)!='#' && w.at(y).at(x-1)>z+1) {
            if(y!=y2 || x-1!=x2) h.push_back({y,x-1});
            w.at(y).at(x-1)=z+1;
        }
    }
    cout << w.at(y2).at(x2) << endl;

    return 0;
}