#include<bits/stdc++.h>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;


int main(){
    int mod=1000000007;
    int n,m,x,y;
    scanf("%d %d",&n,&m);
    //bool c[n][n]={0};
    bool c[n][n];
    for (int i=0;i<n;i++) {
        for (int j=0;j<n;j++) {
            c[i][j]=false;
        }
    }
    for (int i=0;i<m;i++) {
        scanf("%d %d",&x,&y);
        c[x-1][y-1]=true;
        c[y-1][x-1]=true;
    }
    int ans=1;
    for (int i=0;i<(1<<n);i++) {
        //bool d[n]={0};
        bool d[n];
        for (int a=0;a<n;a++) {
            d[a]=false;
        }
        for (int j=0;j<n;j++) {
            if (i>>j & 1) {
                d[j]=true;
            }
        }
        int f=0;
        for (int p=0;p<n;p++) {
            for (int q=p+1;q<n;q++) {
                if (d[p] && d[q]) {
                    if (c[p][q]==false) {
                        f=1;
                        break;
                    }
                }
            }
            if (f==1) break;
        }
        int chk=0;
        if (f==0) {
            for (int x=0;x<n;x++) {
                if (d[x]==true) chk++;
            }
        }

        ans=max(ans,chk);
    }
    printf("%d\n",ans);
    return 0;
}
