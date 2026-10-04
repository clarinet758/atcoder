#include <bits/stdc++.h>
using namespace std;

int main() {
  int N, A;
  cin >> N >> A;

  // ここにプログラムを追記
  for (int i = 0; i < N; i++) {
    string op;
    int p;
    cin >> op >> p;
    if (op == "/" && p == 0) {
      cout << "error" << endl;
      break;
    }
    cout << i + 1 << ":";
    if (op == "+") A += p;
    if (op == "-") A -= p;
    if (op == "*") A *= p;
    if (op == "/") A /= p;
    cout << A << endl;
  }
}
