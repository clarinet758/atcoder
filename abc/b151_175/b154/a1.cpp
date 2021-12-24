#include<bits/stdc++.h>
using namespace std;

int main(){
    int a,b,ans;
    string s,t,u;
    cin >> s >>t;
    cin >> a >> b;
    cin >> u;
    printf("%d %d\n",a-(s==u),b-(t==u));
    return 0;
}
