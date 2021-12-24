#include<bits/stdc++.h>
using namespace std;

#define sc3(a,b,c)  scanf("%d %d %d",&a,&b,&c)

int main(){
    int a,b,c,ans;
    sc3(a,b,c);
    printf("%s\n",((a+b+c)<=21)?"win":"bust");
    return 0;
}
