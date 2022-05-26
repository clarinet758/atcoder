#include<bits/stdc++.h>
using namespace std;

#define sc1(a)  scanf("%d",&a)
#define sc2(a,b)  scanf("%d %d",&a,&b)

int main(){
    int k,a,b;
    sc1(k);
    sc2(a,b);
    printf("%s\n",(a%k==0 || b/k>a/k)?"OK":"NG");
    return 0;
}
