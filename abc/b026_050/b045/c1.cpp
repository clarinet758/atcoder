#include<bits/stdc++.h>
 
using namespace std;
 
#define PI 3.1415926535897932
 
int main(){
    int n,m;
    char s[10];
    long long tmp=0,ans=0;
    scanf("%s",s);
    for (int i=0;i<(1<<(strlen(s)-1));i++) {
        tmp=(s[0]-'0');
        for (int j=0;j<(strlen(s)-1);j++) {
            if (i & (1<<j)) {
                tmp*=10;
                tmp+=(s[j+1]-'0');
            } else {
                ans+=tmp;
                tmp=(s[j+1]-'0');
            }
        }
        ans+=tmp;
    }
    printf("%lld\n",ans);
    return 0;
}
