#include<bits/stdc++.h>

using namespace std;

#define PI 3.1415926535897932


int main(){
    char s[200001];
    int ans=-1,chk=-1;
    scanf("%s",s);
    for (int i=0;i<strlen(s);i++) {
        if (s[i]=='A' && ans==-1) ans=i;
        if (s[i]=='Z') chk=i;
    }
    printf("%d\n",chk-ans+1);
    return 0;
}
