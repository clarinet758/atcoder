#include<bits/stdc++.h>

using namespace std;

#define PI 3.1415926535897932

int main(){
    char a[10],b[10],c[10];
    scanf("%s %s %s",a,b,c);
    printf("%s\n",a[strlen(a)-1]==b[0] && b[strlen(b)-1]==c[0]?"YES":"NO");
    return 0;
}
