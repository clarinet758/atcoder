#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)
#define sc2(a,b)  scanf("%d %d",&a,&b)


int main(){
    int mod=1000000007;
    int n,cnt=0;
    double ans=0.0;
    
    sc1(n);
    vector <int> w(n);
    rep(i,n) w.at(i)=i;
    vector <vector<int>>  t(n,vector<int>(2));
    rep(i,n)  sc2(t.at(i).at(0),t.at(i).at(1)); 
    do {
        cnt++;
        rep(i,n-1) {
            ans+= pow (pow(t.at(w.at(i)).at(0) - t.at(w.at(i+1)).at(0),2) + pow(t.at(w.at(i)).at(1) - t.at(w.at(i+1)).at(1),2),0.5);
        }
    } while (next_permutation(w.begin(),w.end()));
    printf("%.15lf\n",ans/cnt);
    return 0;
}
