#include<bits/stdc++.h>

using namespace std;

int main(){
    int mod=1000000007;
    int o=0,p=0,w,h,n,x,y,a;
    scanf("%d %d %d",&w,&h,&n);
    for (int i=0;i<n;i++) {
        scanf("%d %d %d",&x,&y,&a);
        if (a==1) o=max(o,x);
        if (a==2) w=min(w,x);
        if (a==3) p=max(p,y);
        if (a==4) h=min(h,y);
    }
    printf("%d\n",max(w-o,0)*max(h-p,0));
    return 0;
}
