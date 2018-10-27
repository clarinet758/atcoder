#include<bits/stdc++.h>

using namespace std;

#define PI 3.1415926535897932

int main(){
    int n,k,x,y;
    scanf("%d",&n);
    scanf("%d",&k);
    scanf("%d",&x);
    scanf("%d",&y);
    printf("%d\n",x*min(n,k)+max(y*(n-k),0));

    return 0;
}
