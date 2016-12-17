#include<bits/stdc++.h>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<algorithm>
#include<map>
using namespace std;

/**
 * vector<int>ar(3);
 * for(auto&e:ar){
 *     scanf("%d",&e);
 * }
 * sort(ar.begin(),ar.end())
 * int sum=accumulate(ar.begin(),ar.end(),0);
 **/
int sol(int x) {
    x-=1;
    if (x<3) {
        return max(0,x);
    } else if (x%2==1){
        return (1+x/2)*x/2+(x/4+1);
    } else {
        return (1+x/2)*x/2;
    }
}

int main(){
    int mod=1000000007;
    int r,g,b;
    scanf("%d %d %d",&r,&g,&b);

    printf("%d\n",sol(r)+sol(g)+sol(b));

    return 0;
}
