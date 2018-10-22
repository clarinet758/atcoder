#include<bits/stdc++.h>

using namespace std;

#define PI 3.1415926535897932


int main(){
    int mod=1000000007;
    int n,m;
    char o[50],e[50];
    scanf("%s",o);
    scanf("%s",e);
    for (int i=0;i<50;i++) {
        if (o[i]>='a' && o[i]<='z' && e[i]>='a' && e[i]<='z') {
            printf("%c%c",o[i],e[i]);
        } else if (o[i]>='a' && o[i]<='z') {
            printf("%c",o[i]);
        } else {
            break;
        }
    }
    printf("\n");

    return 0;
}
