#include<bits/stdc++.h>
using namespace std;

#define sc1(a)  scanf("%d",&a)

int main(){
    int x;
    sc1(x);
    printf("%s\n",(abs(x-5)==2 || x==5)?"YES":"NO");
    return 0;
}
