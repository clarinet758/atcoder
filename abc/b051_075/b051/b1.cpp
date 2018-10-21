#include<bits/stdc++.h>

using namespace std;

#define PI 3.1415926535897932

int main(){
    int k,s,ans=0;
    scanf("%d %d",&k,&s);
    for (int i=0;i<=k;i++) {
        for (int j=0;j<=k;j++) {
            if (s-i-j>=0 && s-i-j<=k) ans++;
        }
    }
    printf("%d\n",ans);
    return 0;
}
