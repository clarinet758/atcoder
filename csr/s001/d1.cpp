#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    scanf("%d",&n);
    vector<int> a(n);
    for (auto&e:a) scanf("%d",&e);
    sort(a.begin(),a.end());
    for (int i=0;i<n;i++) printf("%d%c",a[i],i<n-1?' ':'\n');
    return 0;
}
