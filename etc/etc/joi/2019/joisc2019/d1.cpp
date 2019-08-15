#include<bits/stdc++.h>
using namespace std;

int main(){
    int mod=1000000007;
    int n,q;
    //bool w[310][310];
    bool w[2010][2010];
    scanf("%d",&n);
    if (n>2000) return 0;

    for (int i=0;i<2010;i++) for (int j=0;j<2010;j++) w[i][j]=0;
    vector<int>  x(n+1);

    for (int i=1;i<=n;i++) {
        int h,a,b;
        scanf("%d %d %d",&h,&a,&b);
        x[i]=h;
        for (int j=max(1,i-b);j<max(1,i-a+1);j++) w[i][j]=1;
        //for (int j=max(1,i-a);j<max(0,i-b-1);j--) w[i][j]=1;
        for (int j=min(2005,i+a);j<min(2005,i+b+1);j++) w[i][j]=1;
    }

    scanf("%d",&q);
    for (int i=0;i<q;i++) {
        int s,t,ans=-1;
        scanf("%d %d",&s,&t);
        for (int j=s;j<t;j++) {
            for (int k=j+1;k<=t;k++) {
                if (w[j][k]==1 && w[k][j]==1) {
                    ans=max(ans,abs(x[j]-x[k]));
                }
            }
        }
        printf("%d\n",ans);
    }
    return 0;
}
