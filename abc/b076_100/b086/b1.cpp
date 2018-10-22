#include<bits/stdc++.h>

using namespace std;

int main(){
    int a,b,tmp;
    scanf("%d %d",&a,&b);
    if (b==b%10) {
        tmp=a*10+b;
    } else if (b==b%100) {
        tmp=a*100+b;
    } else {
        tmp=a*1000+b;
    }
    for (int i=1;i<1000;i++){
        if (i*i==tmp) {
            printf("Yes\n");
            return 0;
        }
    }
    printf("No\n");
    return 0;
}
