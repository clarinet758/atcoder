#include<bits/stdc++.h>
using namespace std;

#define sc1(a)  scanf("%d",&a)

int main(){
    int n,m,ans;
    sc1(n);
    printf("%d\n",(n/100*111)>=n?n/100*111:(n/100+1)*111);
    return 0;
}
