#include<bits/stdc++.h>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;


int main(){
    int mod=1000000007;
    int n,k;
    scanf("%d %d",&n,&k);
    vector<int> r(n);
    for (auto&e:r) {
        scanf("%d",&e);
    }
    sort(r.begin(), r.end());
    double ans=0;
    for (int i=n-k;i<n;i++) {
        ans=(ans+r[i])/2;
    }
    printf("%.10f\n",ans);

    return 0;
}
