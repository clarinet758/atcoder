#include<bits/stdc++.h>
using namespace std;

int main(){
    int t;
    char s[100020];
    scanf("%s",&s);
    t=strlen(s);
//dream dreamer erase eraser
    for (int i=0;i<(t-5);i++) {
        if (s[i]=='e' && s[i+1]=='r' && s[i+2]=='a' && s[i+3]=='s' && s[i+4]=='e' && s[i+5]=='r') {
            for (int j=0;j<6;j++) s[i+j]='#';
        }
    }
    for (int i=0;i<(t-4);i++) {
        if (s[i]=='e' && s[i+1]=='r' && s[i+2]=='a' && s[i+3]=='s' && s[i+4]=='e') {
            for (int j=0;j<5;j++) s[i+j]='#';
        }
    }
    for (int i=0;i<(t-6);i++) {
        if (s[i]=='d' && s[i+1]=='r' && s[i+2]=='e' && s[i+3]=='a' && s[i+4]=='m' && s[i+5]=='e' && s[i+6]=='r') {
            for (int j=0;j<7;j++) s[i+j]='#';
        }
    }
    for (int i=0;i<(t-4);i++) {
        if (s[i]=='d' && s[i+1]=='r' && s[i+2]=='e' && s[i+3]=='a' && s[i+4]=='m') {
            for (int j=0;j<5;j++) s[i+j]='#';
        }
    }
    for (int i=0;i<t;i++) {
        if (s[i]!='#') {
            printf("NO\n");
            return 0;
        }
    }
    printf("YES\n");

    return 0;
}
