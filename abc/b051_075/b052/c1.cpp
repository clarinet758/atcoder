#include<bits/stdc++.h>

using namespace std;

int main(){
    int n,mod=1000000007;
    long long ans=1;
    bool p[1100];
    int  l[1100];
    for (int i=0;i<1100;i++) {
        p[i]=0;
        l[i]=0;
    }      
    p[2]=1;
    for (int i=3;i<1100;i++) {
        int f=1;
        int t=2;
        while (t*t<=i) {
            if (i%t==0){
                f=0;
                break;
            }
            t++;
        }
        p[i]=f;
     }

//     for (int i=0;i<1100;i++) if (p[i]==1) printf("%d\n",i);

     scanf("%d",&n);
     for (int i=2;i<=n;i++) {
        int tmp=i;
        int cnt=0;
        for (int j=2;j<=n;j++) {
            if (p[j]==1) {
                for (;;) {
                    if (tmp%j==0) {
                        cnt++;
                        tmp/=j;
                    } else {
                        break;
                    }
                }
            } 
        }
        for (int k=0;k<cnt;k++) l[i]++;
    }
/**
6:1,2,3,6
5:1,5
4:1,2,4
3:1,3
2:1,2
1:1
**/
    for (int i=0;i<1100;i++) {
        int tmp=1;
        for (int j=0;j<l[i];j++) {
            tmp*=2;
        }
        ans*=tmp;
        ans%=mod;
    }
    printf("%lld\n",ans);
    return 0;
}
