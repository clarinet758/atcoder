#include<bits/stdc++.h>
using namespace std;

int main(){
    int mod=1000000007;
    int n,ans=1; 
    string s;
    cin >> n;
    cin >>s;
    for (int i=1;i<s.size();i++) {
        if (s.at(i-1)!=s.at(i)) ans++;
    }
    printf("%d\n",ans);
    return 0;
}
