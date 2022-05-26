#include<bits/stdc++.h>
using namespace std;

#define sc2(a,b)  scanf("%d %d",&a,&b)

int main(){
    int n,d;
    sc2(n,d);
    printf("%d\n",n/(d*2+1)+(n%(d*2+1)>0));
    return 0;
}
