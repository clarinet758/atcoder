#include <bits/stdc++.h>
using namespace std;
//20260420
int main() {
  int A, B, C;
  cin >> A >> B >> C;
  vector<int> v={A,B,C};
  sort(v.begin(),v.end());
  cout << v.at(2)-v.at(0) << endl;
}