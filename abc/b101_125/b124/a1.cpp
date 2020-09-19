#include<bits/stdc++.h>
using namespace std;

#define sc2(a,b)  scanf("%d %d",&a,&b)

int main(){
    int a,b,ans=0;
    sc2(a,b);
    ans=max(a*2-1,max(b*2-1,a+b));
    printf("%d\n",ans);
    return 0;
}
