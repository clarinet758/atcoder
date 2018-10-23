#include<bits/stdc++.h>

using namespace std;

int main(){
    int a,b,c;
    scanf("%d %d %d",&a,&b,&c);
    printf("%s\n",(a==5 || a==7) && (b==5 || b==7) && (c==5 || c==7) && (a+b+c==17)?"YES":"NO");

    return 0;
}
