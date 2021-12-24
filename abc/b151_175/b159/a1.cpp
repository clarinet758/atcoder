#include<bits/stdc++.h>
using namespace std;

#define sc2(a,b)  scanf("%d %d",&a,&b)

int main(){
    int n,m;
    sc2(n,m);
    printf("%d\n",n*(n-1)/2+m*(m-1)/2);
    return 0;
}
