#include<bits/stdc++.h>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;


int main(){
    int n;
    char c;
    scanf("%d",&n);
    vector<int>chk(4);
    for(int i=0;i<4;i++){
        chk[i]=0;
    }
    
    for(int i=0;i<n+1;i++){
        scanf("%c",&c);
        if(c!='\n') chk[c-49]++;
    }
    printf("%d %d\n",*max_element(chk.begin(),chk.end()), *min_element(chk.begin(),chk.end()));

    return 0;
}
