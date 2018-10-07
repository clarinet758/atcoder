#include<bits/stdc++.h>

using namespace std;

#define PI 3.1415926535897932

int main(){
    int n,t,x,y,tmp;
    int d[3]={0};
    scanf("%d",&n);
    for (int i=0;i<n;i++) {
        scanf("%d %d %d",&t,&x,&y);
        tmp=abs(x-d[1])+abs(y-d[2]);
        if (t-d[0]>=tmp && ((t-d[0])-tmp)%2==0) {
            d[0]=t,d[1]=x,d[2]=y;
        } else {
            printf("No\n");
            return 0;
        }
    }
    printf("Yes\n");
    return 0;
}

