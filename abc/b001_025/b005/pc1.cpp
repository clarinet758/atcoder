#include<bits/stdc++.h>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;


int main(){
    int mod=1000000007;
    int t,n,m,ans=0;
    scanf("%d",&t);
    scanf("%d",&n);
    vector<int> a(n);
    for(auto&e:a) {
        scanf("%d",&e);
    }
    scanf("%d",&m);
    vector<int> b(m);
    for(auto&e:b) {
        scanf("%d",&e);
    }
    for (auto&e:a) {
        scanf("%d",&e);
    }

    for (int i=0;i<m;i++) {
        for (int j=0;j<n;j++) {
            if (a[j]!=0 && b[i]>=a[j] && b[i]<=a[j]+t) {
                ans+=1;
                a[j]=0;
                break;
            }
        }
    }
    printf((ans==m)?"yes\n":"no\n");
    return 0;
}
