#include<bits/stdc++.h>
using namespace std;

#define sc3(a,b,c)  scanf("%d %d %d",&a,&b,&c)

int main(){
    int mod=1000000007;
    int a,b,c,t,h;
    sc3(a,b,c);
    t=min(a,min(b,c));
    h=(a+b+c)-t-max(a,max(b,c));
    printf("%d\n",t*h/2);
    return 0;
}
