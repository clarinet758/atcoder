#include<bits/stdc++.h>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;


int main(){
    int mod=1000000007;
    int n,m;
    int N[10];
    for (int i=0;i<10;i++) {
        scanf("%d" ,&N[i]);
    }
    scanf("%d",&n);
    long long l[n];
    for (int i=0;i<n;i++) {
        scanf("%lld",&l[i]);
    }

    vector<long long> chikan(n);
    for (int i=0;i<n;i++) {
        int s=l[i];
        int tmp=1;
        chikan[i]=0;
        for (;;) {
            for (int j=0;j<10;j++) {
                if (s%10==N[j]) {
                    chikan[i]=chikan[i]+(j*tmp);
                    break;
                }
            }
            s=s/10;
            tmp=tmp*10;
            if (s==0) break;
        }
    }
    sort(chikan.begin(),chikan.end());
    for (int i=0;i<n;i++) {
        int s=chikan[i];
        int ans=0;
        int tmp=1;
        for (;;) {
            ans=ans+(N[s%10]*tmp);

            tmp=tmp*10;
            s=s/10;
            if (s==0) break;
        }
        printf("%d\n",ans);
    }
    return 0;
}
