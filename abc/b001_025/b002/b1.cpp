#include<bits/stdc++.h>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;


int main(){
    int mod=1000000007;
    char w[31];
    scanf("%s",w);
    int chk=strlen(w);
    for (int i=0;i<chk;i++){
        if (w[i]!='a' && w[i]!='i' && w[i]!='u' && w[i]!='e' && w[i]!='o') {
            printf("%c",w[i]);
        }
    }
    printf("\n");
    return 0;
}
