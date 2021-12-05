#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)

int main(){
    int n,p;
    string s;
    bool ans=1;
    cin >> n;
    cin >> s;
    p=s.size();
    if (p%2==1) ans=0;
    if(p%2==0) for(int i=0;i<p/2;i++) {
        if (s.at(i)!=s.at(p/2+i)) ans=0;
    }
    cout << (ans?"Yes":"No") << endl;
    return 0;
}
