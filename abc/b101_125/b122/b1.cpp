#include<bits/stdc++.h>
using namespace std;

int main(){
    int cnt=0,ans=0;
    char s[25];
    scanf("%s",s);
    for (long i=0;i<strlen(s);i++) {
        if (s[i]=='A') cnt++;
        else if (s[i]=='C') cnt++;
        else if (s[i]=='G') cnt++;
        else if (s[i]=='T') cnt++;
        else cnt=0;
        ans=max(ans,cnt);
    }
    printf("%d\n",ans);
    return 0;
}
