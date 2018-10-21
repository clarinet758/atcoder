#include<bits/stdc++.h>

using namespace std;

#define PI 3.1415926535897932

int main(){
    int mod=1000000007;
    int n,m;
    char op[1];
    scanf("%d %c %d",&n,&op,&m);
    printf("%d\n",op[0]=='+'?n+m:n-m);

    return 0;
}
