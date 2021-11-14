#include <bits/stdc++.h>
using namespace std;
 
int main() {
  string S;
  cin >> S;
  int x=1, l =  S.size();
  for (int i = 1;i < l;i++) {
      if (S.at(i) == '+') x++;
      else x--;
      i++;
  }
  cout << x << endl;
}