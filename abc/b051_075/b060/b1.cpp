#include<bits/stdc++.h>

using namespace std;

#define PI 3.1415926535897932

int main(){
    int a,b,c;
    scanf("%d %d %d",&a,&b,&c);
    printf("%s\n",c%__gcd(a,b)==0?"YES":"NO");
    return 0;
}
