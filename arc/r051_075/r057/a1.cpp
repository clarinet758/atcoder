#include<bits/stdc++.h>
using namespace std;

int main(){
    long long a,k,chk=2000000000000;
    scanf("%lld %lld",&a,&k);
    if (k==0) {
        printf("%lld\n",chk-a);
    } else {
        for (int i=1;;i++) {
            a+=1+a*k;
            if (a>=chk) {
                printf("%d\n",i);
                break;
            }
        }
    }
    return 0;
}
