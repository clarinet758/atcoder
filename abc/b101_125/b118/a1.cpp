#include<bits/stdc++.h>
using namespace std;

#define sc2(a,b)  scanf("%d %d",&a,&b)

int main(){
    int a,b;
    sc2(a,b);
    printf("%d\n",b%a==0?a+b:b-a);
    return 0;
}
