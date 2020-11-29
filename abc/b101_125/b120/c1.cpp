#include<bits/stdc++.h>
using namespace std;

int main(){
    int n=0,m=0;
    char s[100005];
    scanf("%s",s);
    for (long i=0;i<strlen(s);i++) {
        n+=s[i]=='0';
        m+=s[i]=='1';
    }
    printf("%d\n",min(n,m)*2);
    return 0;
}
