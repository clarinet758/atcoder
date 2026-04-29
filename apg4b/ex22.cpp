#include <bits/stdc++.h>
using namespace std;
//20260430
int main(){
    int N;
    cin >> N;
    vector<pair<int, int>> p(N);
    for (int i=0;i<N;i++){
        cin >> p.at(i).second >> p.at(i).first;
    }
    sort(p.begin(),p.end());
    for (int i=0;i<N;i++){
        cout << p.at(i).second << " " << p.at(i).first << endl;
    }
}