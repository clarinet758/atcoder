#include<bits/stdc++.h>

using namespace std;

int main(){
    vector<int> a(5);
    for(auto&e:a) scanf("%d",&e);
    for (int i=1;i<5;i++){
        if (a[i]==a[i-1]) {
            printf("YES\n"); 
            return 0;
        }
    }
    printf("NO\n");
    return 0;
}
