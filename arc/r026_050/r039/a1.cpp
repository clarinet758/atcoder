#include<bits/stdc++.h>
using namespace std;

int main(){
    int a,b,tmp,ans;
    scanf("%d %d",&a,&b);
    if (a/900 && (a%100)/90) tmp=999;
    else if (a/900) tmp=990+a%10;
    else tmp=900+a%100;
    ans=tmp-b;
    if (b/100==1 && b%100<10) tmp=100;
    else if (b/100==1) tmp=100+b%10;
    else tmp=100+b%100;
    ans=max(ans,a-tmp);
    printf("%d\n",ans);
    return 0;
}
