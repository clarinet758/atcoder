#include <bits/stdc++.h>
using namespace std;
//20260420
int main() {
  int N;
  cin >> N;
  int a=0;
  vector<int> v(N);
  for(int i=0;i<N;i++){
    cin >> v.at(i);
    a+=v.at(i);
  }

  for(int i=0;i<N;i++){
    cout << abs(a/N-v.at(i)) << endl;
  }
}