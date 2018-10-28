#include<bits/stdc++.h>

using namespace std;

int main(){
    vector<int> a(3);
    for (auto&e:a) {
        scanf("%d",&e);
    }
    sort(a.begin(),a.end());
    printf("%s\n",a[2]==a[1]+a[0]?"Yes":"No");
    return 0;
}
