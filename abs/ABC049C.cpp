#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)

int main(){
    int n;
    string s;
    cin >> s;
    n=s.size()-1;
    for(;;) {
        if(n>3) {
            if (s.at(n)=='e' && s.at(n-1)=='s' && s.at(n-2)=='a' && s.at(n-3)=='r' && s.at(n-4)=='e') {
                n-=5;
                continue;
            } else if (s.at(n)=='m' && s.at(n-1)=='a' && s.at(n-2)=='e' && s.at(n-3)=='r' && s.at(n-4)=='d') {
                n-=5;
                continue;
            }
        }
        if(n>4) {
            if (s.at(n)=='r' && s.at(n-1)=='e' && s.at(n-2)=='s' && s.at(n-3)=='a' && s.at(n-4)=='r' && s.at(n-5)=='e') {
                n-=6;
                continue;
            }
        } 
        if(n>5) {
            if (s.at(n)=='r' && s.at(n-1)=='e' && s.at(n-2)=='m' && s.at(n-3)=='a' && s.at(n-4)=='e' && s.at(n-5)=='r' && s.at(n-6)=='d') {
                n-=7;
                continue;
            }
        }
        if(n==-1) break;
        //cout << n << endl;
        cout << "NO" << endl;
        return 0;
    }
    cout << "YES" << endl;
    return 0;
}
