#include<bits/stdc++.h>
using namespace std;

int main(){
    string s;
    cin >> s;
    for (int i=0;i<s.size();i++){
        if (i%2) {
            if (s.at(i)=='R') {

                cout << "No" << endl;
                return 0;
            }
        } else {
            if (s.at(i)=='L') {
                cout << "No" << endl;
                return 0;
            }
        }
    } 
    cout << "Yes" << endl;
    return 0;
}
