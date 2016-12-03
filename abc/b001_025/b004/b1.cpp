#include<bits/stdc++.h>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;


int main(){
    int mod=1000000007;
    int n,m;
    char c[4][4];
    for (int i=0;i<4;i++){
        for (int j=0;j<4;j++) {
            scanf(" %c",&c[i][j]);
        }
    }
    for (int i=3;i>=0;i--){
        for (int j=3;j>=0;j--) {
            printf("%c ",c[i][j]);
        }
        printf("\n");
    }


    return 0;
}
