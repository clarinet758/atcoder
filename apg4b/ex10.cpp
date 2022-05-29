#include <bits/stdc++.h>
using namespace std;
 
int main() {
  int A, B, x=0;
  cin >> A >> B;
 
  // ここにプログラムを追記
  cout << "A:";
  while (x<A) {
    cout << "]";
    x++;
  }
  cout << endl;
  x=0;
  cout << "B:";
  while (x<B) {
    cout << "]";
    x++;
  }
  cout << endl;
}