#include<bits/stdc++.h>
using namespace std;

int main(){
    string s;
    cin >> s;
    printf("%s\n",(s.at(0)==s.at(1) && s.at(1)==s.at(2))?"No":"Yes");
    return 0;
}
