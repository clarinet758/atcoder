#include <bits/stdc++.h>
using namespace std;
//20260419
int main() {
  int A, B;
  string op;
  cin >> A >> op >> B;

  if (op == "+") {
    cout << A + B << endl;
  } else if (op == "-") {
    cout << A - B << endl;
  }
  else if (op == "*") {
    cout << A * B << endl;
  }
  else if (op == "/"  && B != 0) {
    cout << A / B << endl;
  }  else {
    cout << "error" << endl;
  }
}