#include<bits/stdc++.h>
using namespace std;
int main(){
    char s[100000];
    scanf("%s",s);
    for (int i=0;i<strlen(s)-2;i++) {
        if (s[i]==s[i+1] || s[i]==s[i+2] || s[i+1]==s[i+2]) {
//        if (s[i]==s[i+1] || s[i]==s[i+2]) {
            printf("%d %d\n",i+1,i+3);
            return 0;
        }
    }
    if (strlen(s)==2 && s[0]==s[1]) printf("1 2\n");
    else printf("-1 -1\n");
    return 0;
}
