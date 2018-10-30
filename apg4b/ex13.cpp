#include<bits/stdc++.h>

using namespace std;

int main(){
    int mod=1000000007;
    int n;
    scanf("%d",&n);
    vector<int> a(n);

    for (auto&e:a) scanf("%d",&e);
    int avg=accumulate(a.begin(),a.end(),0);
    avg/=n;
    for (int i=0;i<n;i++) printf("%d\n",abs(a[i]-avg));

    return 0;
}
