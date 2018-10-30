#include<bits/stdc++.h>

using namespace std;

int main(){
    char s[101];
    scanf("%s",s);
    int ans=1;
    if (strlen(s)==1) {
        printf("1\n");
    } else {
        for (int i=1;i<strlen(s);i++) {
            if (s[i]=='+') ans++;
            if (s[i]=='-') ans--;
            i++;
        }
        printf("%d\n",ans);
    }
    return 0;
}
