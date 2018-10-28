#include<bits/stdc++.h>

using namespace std;

int main(){
    char s[100001];
    scanf("%s",s);
    int a,c=0,t;
    t=strlen(s);
    a=s[0]=='B'?0+'B':0+'W';
    for (int i=0;i<t;i++) {
        if (0+s[i]!=a) {
            c++;
            a=0+s[i];
        }
    }
    printf("%d\n",c);
    return 0;
}
