#include <bits/stdc++.h>
using namespace std;

int main() {
    int n,a,b;
    scanf("%d",&n);
    scanf("%d",&a);
    char op[5];
    for (int i=1;i<=n;i++) {
        scanf("%s %d",op,&b);
        //cin>>op>>b;
        if (op[0]=='/' && b==0) {
            printf("error\n");
            break;
        }
//        printf("%c\n",op[0]);
        if (op[0]=='+') {
            a+=b;
        } else if(op[0]=='-') {
            a-=b;
        } else if(op[0]=='*') {
            a*=b;
        } else if(op[0]=='/') {
            a/=b;
        }
        printf("%d:%d\n",i,a);
    }
    return 0;
} 
