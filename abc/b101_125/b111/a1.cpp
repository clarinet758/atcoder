#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)

int main(){
    char s[5];
    scanf("%s",s);
    rep(i,3) {
        if (s[i]=='1') printf("%c",'9');
        else if (s[i]=='9') printf("%c",'1'); 
        else printf("%c",s[i]);
    }
    puts("");
    return 0;
}
