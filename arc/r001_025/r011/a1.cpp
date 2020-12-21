#include<bits/stdc++.h>
using namespace std;

#define sc3(a,b,c)  scanf("%d %d %d",&a,&b,&c)

int main(){
    int n,m,x,tmp=0,ans=0;
    sc3(m,n,x);
    while(x>0){
        ans+=x;
        x+=tmp;
        tmp=x%m;
        x=(x/m)*n;
    }
    printf("%d\n",ans);
    return 0;
}
