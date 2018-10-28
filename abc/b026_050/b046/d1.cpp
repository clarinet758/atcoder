#include<bits/stdc++.h>

using namespace std;

int main(){
    char s[100001];
    int ans=0;
    scanf("%s",s);
    for (int i=0;i<strlen(s);i++) {
        if (i%2==0) ans+=(s[i]=='g'?0:-1);
        if (i%2 && s[i]=='g') ans++;
    }
    printf("%d\n",ans);
    return 0;
}
