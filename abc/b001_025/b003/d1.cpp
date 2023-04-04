#include<bits/stdc++.h>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;
//long long mod=1000000007;

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
                //b[j]=(a[j]+a[j-1])%mod;
                1;
            }
        }
        tmp++;
        memcpy(a,b,sizeof(b));
        long b[1000];
    }
    return a[r];
}


const int MAX=510000;
const int MOD=1000000007;
 
long long fac[MAX], finv[MAX], inv[MAX];

//前処理 
void COMinit() {
    fac[0]=fac[1]=1;
    finv[0]=finv[1]=1;
    inv[1]=1;
    for (int i=2;i<MAX;i++) {
        fac[i]=fac[i-1]*i%MOD;
        inv[i]=MOD-inv[MOD%i]*(MOD/i)%MOD;
        finv[i]=finv[i-1]*inv[i]%MOD;
    }
}
//二項係数計算
long long COM(int n,int k) {
    if (n<k) return 0;
    if (n<0 || k<0) return 0;
    return fac[n]*(finv[k]*finv[n-k]%MOD)%MOD;
}


int main(){
    int mod=1000000007;
    int r,c,x,y,d,l,ans=1;
    scanf("%d %d",&r,&c);
    scanf("%d %d",&x,&y);
    scanf("%d %d",&d,&l);
    
    COMinit();
    if (x*y>(d+l)) cout << (r-x+1)*(c-y+1)%mod*(COM(d+l,d)%mod)*(COM(x*y,d+l)-COM((x-1)*y,d+l)-COM((x-1)*y,d*l)-COM(x*(y-1),d+l)-COM(x*(y-1),d+l)%mod)%mod << endl;
    else cout << (r-x+1)*(c-y+1)%mod*COM(d+l,d)%mod<< endl;

    return 0;
}
