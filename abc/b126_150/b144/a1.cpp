#include<bits/stdc++.h>
using namespace std;

#define sc2(a,b)  scanf("%d %d",&a,&b)

int main(){
    int a,b;
    sc2(a,b);
    printf("%d\n",(a<10 && b<10)?a*b:-1);
    return 0;
}
