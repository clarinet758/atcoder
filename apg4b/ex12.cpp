#include <bits/stdc++.h>
using namespace std;

int main() {
  string S;
  cin >> S;

  // ここにプログラムを追記
  int x = S.size(),ans=1;
  for (int i=0;i<x;i++) {
    if (S.at(i) == '+') ans++;
    if (S.at(i) == '-') ans--;
  }
  cout << ans << endl;

}
