#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <bitset>
#include <numeric>
#include <utility>
#include <iomanip>
#include <algorithm>
#include <functional>
#include <unordered_map>
using namespace std;

template<class T> inline bool chmax(T& a, T b) { if (a < b) { a = b; return 1; } return 0; }
template<class T> inline bool chmin(T& a, T b) { if (a > b) { a = b; return 1; } return 0; }


int n,k;
vector<int> a;

void solve() {
    vector<long long> vs;
    map<long long, vector<int>> pl;
    for (int i = 0; i < a.size(); ++i) {
        vs.push_back(a[i]);
        pl[a[i]].push_back(i);
    }
    sort(vs.begin(), vs.end());
    vs.erase(unique(vs.begin(), vs.end()), vs.end());

    int s = vs.size();
    vector<long long> dp(s+1, 0);
    for (int i = 0; i < N; ++i) {
        int it = lower_bound(vs.begin(), vs.end(), a[i]) - vs.begin();
        if (it == 0 || a[i] != vs[it-1] + 1) dp[it] = 1;
        else chmax(dp[it], dp[it-1] + 1);
    }

    long long res = 0;
    long long val = -1;
    for (int i = 0; i <= s; ++i) if (chmax(res, dp[i])) val = vs[i];

    vector<int> ans;
    int end = N;
    for (int i = 0; i < res; ++i) {
        int it = lower_bound(pl[val].begin(), pl[val].end(), end) - pl[val].begin();
        --it;
        ans.push_back(pl[val][it]);
        end = pl[val][it];
        --val;
    }
    reverse(ans.begin(), ans.end());
    
    cout << res << endl;
    for (int i = 0; i < res; ++i) {
        if (i) cout << " ";
        cout << ans[i]+1;
    }
    cout << endl;
}

int main() {
    scanf("%d %d",&n,&k);
    for (int i=0;i<n;i++){
        int aa;
        scanf("%d",&aa);
        a.push_back(aa);
    }
    solve();
}