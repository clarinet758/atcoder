#include <bits/stdc++.h>
using namespace std;

int main() {
  int N, a = 0;
  cin >> N;
  vector<int> v(N);
  for (int i = 0; i < N; i++) {
    cin >> v.at(i);
    a += v.at(i);
  }
  a /= N;
  for (int i = 0; i < N; i++) {
    cout << abs(v.at(i) - a) << endl;
  }
}
