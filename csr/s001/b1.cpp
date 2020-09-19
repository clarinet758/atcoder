#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    scanf("%d",&n);
    vector <int>a(n);
    for (auto&e:a) scanf("%d",&e);
    printf("%d\n",accumulate(a.begin(),a.end(),0));
    return 0;
}
