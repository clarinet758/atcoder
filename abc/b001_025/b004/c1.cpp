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
    int s[6]={1,2,3,4,5,6};
    scanf("%d",&n);
    n%=30;
    for (int i=0;i<n;i++) {
        swap(s[i%5],s[(i%5+1)]);
    }
    for (int i=0;i<6;i++) {
        printf("%d",s[i]);
    }
    printf("\n");
    return 0;
}
