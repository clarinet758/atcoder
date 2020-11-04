#include<bits/stdc++.h>
using namespace std;

#define sc3(a,b,c)  scanf("%d %d %d",&a,&b,&c)

int main(){
    int a,b,c;
    sc3(a,b,c);
    printf("%d\n",min(b/a,c));
    return 0;
}
