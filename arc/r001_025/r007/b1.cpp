#include<bits/stdc++.h>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;


int main(){
    int mod=1000000007;
    int n,m,t;
    scanf("%d %d",&n,&m);
    int cd[n+1];
    for (int i=0;i<n+1;i++) {
        cd[i]=i;
    }
    for (int i=0;i<m;i++) {
        scanf("%d",&t);
        int tmp=cd[0];
        for (int j=1;j<n+1;j++) {
            if (cd[j]==t) {
                cd[0]=cd[j];
                cd[j]=tmp;
            }
        }
    }

    for (int i=1;i<n+1;i++) {
        printf("%d\n",cd[i]);
    }
    return 0;
}
