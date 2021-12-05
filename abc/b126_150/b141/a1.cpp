#include<bits/stdc++.h>
using namespace std;

int main(){
    string s;
    cin >> s;
    if (s.at(0)=='S') {
        cout << "Cloudy" << endl;
    } else if (s.at(0)=='C') {
        cout << "Rainy" << endl;
    } else {
        cout << "Sunny" << endl;
    }
    return 0;
}
