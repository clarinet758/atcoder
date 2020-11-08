#include<bits/stdc++.h>
using namespace std;

#define sc3(a,b,c)  scanf("%d %d %d",&a,&b,&c)

int main(){
    int a,b,k,ans;
    sc3(a,b,k);
    ans=max(a,b);
    for (int i=ans;ans>0;i--) {
        ans=i;
        if (a%i==0 && b%i==0) k--;
        if(k==0) break;
    }
    printf("%d\n",ans);
    return 0;
}
