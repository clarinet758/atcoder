#include<bits/stdc++.h>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;
long long mod=1000000007;

long long pscl(int n, int r) {
    long tmp=2;
    long a[1000];
    a[0]=1;
    a[1]=1;
    long b[1000];
    for (int i=2;i<=n;i++) {
        for (int j=0;j<tmp+1;j++) {
            if (j==0 || j==tmp) {
                b[j]=1;
            } else {
                b[j]=(a[j]+a[j-1])%mod;
            }
        }
        tmp++;
        memcpy(a,b,sizeof(b));
        long b[1000];
    }
    return a[r];
}



int main(){
    int mod=1000000007;
    int r,c,x,y,d,l,ans;
    scanf("%d %d",&r,&c);
    scanf("%d %d",&x,&y);
    scanf("%d %d",&d,&l);
    printf("%d\n",pscl(d+l,max(d,l))*((r+1)-x)*((c+1)-y)%mod);
    return 0;
}
