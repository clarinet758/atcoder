#include<bits/stdc++.h>
using namespace std;

int main(){
    int n,ans=0,tmp=0;
    char s[110];
    scanf("%d",&n);
    scanf("%s",s);
    for (int i=0;i<n;i++) {
        tmp+=s[i]=='I'?1:-1;
        ans=max(ans,tmp);
    }
    printf("%d\n",ans);
    return 0;
}
