#include<bits/stdc++.h>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;


int main(){
    int mod=1000000007;
    int n,m;
    char s[11],t[11];
    scanf("%s",s);
    scanf("%s",t);
    int chk=strlen(s);
    for (int i=0;i<chk;i++) {
        if (s[i]==t[i]) {
            continue;
        } else if (s[i]=='@' && (t[i]=='a' || t[i]=='t' || t[i]=='c' || t[i]=='o' || t[i]=='d' || t[i]=='e' || t[i]=='r')) {
            continue;
        } else if (t[i]=='@' && (s[i]=='a' || s[i]=='t' || s[i]=='c' || s[i]=='o' || s[i]=='d' || s[i]=='e' || s[i]=='r')) {
            continue;
        } else {
            printf("You will lose\n");
            return 0;
        }
    }
    printf("You can win\n");

    return 0;
}
