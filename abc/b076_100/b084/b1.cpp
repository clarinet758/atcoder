#include<bits/stdc++.h>
using namespace std;

int main(){
    int a,b;
    scanf("%d %d",&a,&b);
    char s[a+b+5];
    scanf("%s",s);
    for (int i=0;i<(a+b+1);i++) {
        if (i==a && isdigit(s[i])) {
            printf("No\n");
            return 0;
        } else if (i!=a && isdigit(s[i])==false) {
            printf("No\n");
            return 0;
        }
    }
    printf("Yes\n");
    return 0;
}
