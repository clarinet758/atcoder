#include<bits/stdc++.h>

using namespace std;

#define PI 3.1415926535897932

int main(){
    char a[102],b[102];
    scanf("%s",a);
    scanf("%s",b);
    if (strlen(a)>strlen(b)) {
        printf("GREATER\n");
        return 0;
    } else if (strlen(a)<strlen(b)) {
        printf("LESS\n");
        return 0;
    }
    for (int i=0;i<strlen(a);i++) {
        if (a[i]-0>b[i]-0) {
            printf("GREATER\n");
            return 0;
        } else if (a[i]-0<b[i]-0) {
            printf("LESS\n");
            return 0;
        }
    }
    printf("EQUAL\n");
    return 0;
}
