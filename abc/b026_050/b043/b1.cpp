#include<bits/stdc++.h>

using namespace std;

int main(){
    char s[10];
    char ans[11]={'b','b','b' ,'b','b','b','b','b','b' ,'b','b'};
    scanf("%s",s);
    for (int i=0;i<strlen(s);i++) {
        if (s[i]=='0' || s[i]=='1') {
            for (int j=0;j<10;j++){
                if (ans[j]=='b') {
                    ans[j]=s[i];
                    break;
                }
            }
        } else {
            if (ans[0]!='b') {
                for (int j=1;j<10;j++) {
                    if (ans[j]=='b') {
                        ans[j-1]='b';
                        break;
                    }
                }
            } 
        }
    }

    for (int i=0;i<10;i++) {
        if (ans[i]!='b') {
            printf("%c",ans[i]);
        }
    }
    printf("\n");

    return 0;
}
