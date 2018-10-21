#include<bits/stdc++.h>

using namespace std;

#define PI 3.1415926535897932

int main(){
    char a[1];
    for (int i=0;i<19;i++) {
        scanf("%c",&a);
        printf("%c",a[0]==','?' ':a[0]);
    }
    printf("\n");
    return 0;
}
