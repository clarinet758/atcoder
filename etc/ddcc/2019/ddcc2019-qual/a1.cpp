#include<bits/stdc++.h>
using namespace std;

int main(){
    int mod=1000000007;
    int n,ans=1;
    scanf("%d",&n,&m);
    for (int i=0;i<n;i++) ans*=4;
    printf("%d\n",ans);
    return 0;
}
