#include<bits/stdc++.h>
using namespace std;

#define sc3(a,b,c)  scanf("%d %d %d",&a,&b,&c)

int main(){
    int a,b,c;
    sc3(a,b,c);
    swap(a,b);
    swap(a,c);
    printf("%d %d %d\n",a,b,c);
    return 0;
}
