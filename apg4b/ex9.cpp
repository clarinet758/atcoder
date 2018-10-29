#include <bits/stdc++.h>
using namespace std;

int main() {
    int x,a,b;
    scanf("%d %d %d",&x,&a,&b);
    x++;
    printf("%d\n",x);
    x*=(a+b);
    printf("%d\n",x);
    x*=x;
    printf("%d\n",x);
    x--;
    printf("%d\n",x);
    return 0;
} 
