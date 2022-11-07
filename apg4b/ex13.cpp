#include <bits/stdc++.h>
using namespace std;

int main() {
  int N;
  cin >> N;
  vector<int> w(N,0);
  int t=0;
  for (int i=0;i<N;i++) {
    cin >> w.at(i);
    t+=w.at(i);
  }

  for (int i=0;i<N;i++) cout << abs(t/N-w.at(i)) << endl;
}
