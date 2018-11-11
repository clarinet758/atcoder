#include<bits/stdc++.h>
using namespace std;

int main(){
    int n,t,x,y,tmp;
    int chk[3]={0,0,0};
    scanf("%d",&n);
    for (int i=0;i<n;i++) {
        scanf("%d %d %d",&t,&x,&y);
        tmp=abs(x-chk[1])+abs(y-chk[2]);
        if (tmp>t-chk[0] || ((t-chk[0])-tmp)%2) {
            printf("No\n");
            return 0;
        }
        chk[0]=t;
        chk[1]=x;
        chk[2]=y;
    }
    printf("Yes\n");
    return 0;
}
