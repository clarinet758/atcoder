#include<bits/stdc++.h>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;


int main(){
    int mod=1000000007;
    int n,ans;
    scanf("%d",&n);
    if (n%2==0) {
        ans=(1+n)*(n/2);
    } else {
        ans=(1+n)*(n/2)+((n+1)/2);
    }
    printf("%d\n",ans*10000/n);
    return 0;
}
