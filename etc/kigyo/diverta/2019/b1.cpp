#include<bits/stdc++.h>
using namespace std;

int main(){
    int r,g,b,n,ans=0;
    scanf("%d %d %d %d",&r,&g,&b,&n);
    for (int i=0;i<n+1;i++) {
        for (int j=0;j<n+1;j++) {
            if ((i*r+j*g)>n) break;
            if ((n-(i*r+j*g))%b==0) ans+=1;
        }
    }
    printf("%d\n",ans);
    return 0;
}
