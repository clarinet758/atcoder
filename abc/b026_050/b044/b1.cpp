#include<bits/stdc++.h>

using namespace std;

int main(){
    char w[101];
    int chk[26]={0};
    scanf("%s",w);
    for (int i=0;i<strlen(w);i++){
        chk[w[i]-'a']++;
    }
    for (int i=0;i<26;i++) {
        if (chk[i]%2) {
            printf("No\n");
            return 0;
        }
    }
    printf("Yes\n");
    return 0;
}
