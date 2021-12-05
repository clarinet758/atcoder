#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)

bool w[10000];

int main(){
    int a;
    sc1(a);
    for(int i=1;i<10000;i++){
        if (w[a]) {printf("%d\n",i); break;}
        w[a]=1;
        if(a%2) a=a*3+1;
        else a=a/2;
    }
    return 0;
}
