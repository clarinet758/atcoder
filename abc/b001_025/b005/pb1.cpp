#include<bits/stdc++.h>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;


int main(){
    int mod=1000000007;
    int n,t,ans=101;
    
    scanf("%d",&n);
    for (int i=0;i<n;i++) {
        scanf("%d",&t);
        ans=min(ans,t);
    }
    printf("%d\n",ans);
    return 0;
}
