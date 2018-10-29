#include <bits/stdc++.h>
using namespace std;
 
int main() {
    int a,b;
    char op[1];
    scanf("%d %c %d",&a,op,&b);
    //printf("%s\n",op);
    if (op[0]=='+') {
        printf("%d\n",a+b);
    } else if (op[0]=='-') {
        printf("%d\n",a-b);
    } else if (op[0]=='*') {
        printf("%d\n",a*b);
    } else if (op[0]=='/' && b!=0) {
        printf("%d\n",a/b);
    } else if (op[0]=='/') {
        printf("error\n");
    } else if (op[0]=='?' || op[0]=='!' || op[0]=='=') {
        printf("error\n");
    }
    return 0;
}
