#include<bits/stdc++.h>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;


int main(){
    int mod=1000000007;
    int m;
    scanf("%d",&m);
    if (m<100) {
        printf("00\n");
    } else if (m<=5000) {
        printf("%02d\n",m/100);
    } else if (m>=6000 && m<=30000) {
        printf("%d\n",m/1000+50);
    } else if (m>=35000 && m<=70000) {
        printf("%d\n",(m/1000-30)/5+80);
    } else {
        printf("%d\n",89);
    }
    return 0;
}
