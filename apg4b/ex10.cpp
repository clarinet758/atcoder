#include <bits/stdc++.h>
using namespace std;

int main() {
    int a,b;
    scanf("%d %d",&a,&b);
    printf("A:");
    while (a>0) {
        printf("]");
        a--;
    }
    printf("\n");
    printf("B:");
    while (b>0) {
        printf("]");
        b--;
    }
    printf("\n");
    return 0;
} 
