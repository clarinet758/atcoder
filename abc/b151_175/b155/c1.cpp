#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define per(i,n)  for(int i=n-1;i>=0;--i)
#define sc1(a)  scanf("%d",&a)
#define sc2(a,b)  scanf("%d %d",&a,&b)
#define sc3(a,b,c)  scanf("%d %d %d",&a,&b,&c)

int main(){
    int n,cnt=0;
    map<string, int> w;
    sc1(n);
    rep(i,n) {
        string s;
        cin >> s;
        w[s]+=1;
        cnt=max(cnt,w[s]);
    }
    vector <string> ans;
    for (auto itr=w.begin(); itr!=w.end(); ++itr) {
        if (itr->second==cnt) ans.push_back(itr->first);
    }
    sort(ans.begin(),ans.end());
    for (auto i:ans) {
        cout << i << endl;
    }
    return 0;
}
