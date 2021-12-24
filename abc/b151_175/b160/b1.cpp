#include<bits/stdc++.h>
using namespace std;

#define sc1(a)  scanf("%d",&a)

int main(){
    int x;
    sc1(x);
    printf("%d\n",x/500*1000+x%500/5*5);
    return 0;
}
