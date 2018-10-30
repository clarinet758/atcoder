#include<bits/stdc++.h>

using namespace std;

int main(){
    int n,s,ans=0;
    scanf("%d %d",&n,&s);
    vector<int> a(n);
    vector<int> b(n);
    for (auto&e:a) scanf("%d",&e);
    for (auto&e:b) scanf("%d",&e);
    for (int i=0;i<n;i++) for (int j=0;j<n;j++){
        if (a[i]+b[j]==s) ans++;
    }
    printf("%d\n",ans);
    return 0;
}
