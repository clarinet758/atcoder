#include<bits/stdc++.h>
using namespace std;

int main(){
    int a,b,c,x,y,z,ans;
    scanf("%d %d %d %d %d",&a,&b,&c,&x,&y);
    z=min(x,y);
    ans=min(a*z+b*z,c*z*2)+min(a*(x-z),c*(x-z)*2)+min(b*(y-z),c*(y-z)*2);
    printf("%d\n",ans);
    return 0;
}
