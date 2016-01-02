#include<bits/stdc++.h>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;


int main(){
    int m,n,N,r,ans=0,tmp=0;
    scanf("%d %d %d",&m,&n,&N);
    for(;;){
        ans+=N;
        r=((N+tmp)/m)*n;
        tmp=(N+tmp)%m;
        N=r;
        if(N==0) break;
    }

    printf("%d\n",ans);
    return 0;
}
