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

int main(){
    map<int, int> mp;
    mp={{1,0},{2,1},{3,2},{4,4},{5,6}};
    int mod=1000000007;
    int r,g,b;
    scanf("%d %d %d",&r,&g,&b);
    printf("%d\n",mp[r]+mp[g]+mp[b]);

    return 0;
}
