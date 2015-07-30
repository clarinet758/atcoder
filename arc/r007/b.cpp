#include<bits/stdc++.h>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;


int main(){
    int n,m,d;
    scanf("%d %d",&n,&m);
    int cd[n+1];
    for(int i=0;i<n+1;i++){
        cd[i]=i;
    }
    for(int i=0;i<m;i++){
        scanf("%d",&d);
        for(int j=1;j<n+1;j++){
            if(cd[j]==d){
                swap(cd[0],cd[j]);
                break;
            }
        }
    }

    for(int i=1;i<n+1;i++){
        printf("%d\n",cd[i]);
    }
    return 0;
}
