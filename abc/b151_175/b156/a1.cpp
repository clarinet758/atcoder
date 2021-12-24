#include<bits/stdc++.h>
using namespace std;

#define sc2(a,b)  scanf("%d %d",&a,&b)

int main(){
    int n,r;
    sc2(n,r);
    printf("%d\n",r + 100 * max(0,10-n));
    return 0;
}
