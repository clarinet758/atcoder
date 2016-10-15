#include<bits/stdc++.h>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;


int main(){
    int n;
    //double t=3.305785; 
    scanf("%d",&n);
    long long t=1;
    long long a=1;
    for (int i=0;i<n;i++) {
        long long x;
        long long y;
        scanf("%lld %lld",&x,&y);
        if (t<=x && a<=y) {
            t=x;
            a=y;
        } else {
            int tmp=1;
            for (;;) {
                if (x*tmp>=t && y*tmp>=a) {
                    t=x*tmp;
                    a=y*tmp;
                    break;
                }
                tmp++;
            }
        }
    }
    printf("%lld\n",a+t);
    return 0;
}
