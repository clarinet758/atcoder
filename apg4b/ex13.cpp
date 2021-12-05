#include <bits/stdc++.h>
using namespace std;
 
int main() {
  int N;
  cin >> N;
  vector<int> score(N);
  for (int i=0;i<N;i++)  {
      cin >> score.at(i);
  }
  int avg = accumulate(score.begin(),score.end(),0)/N;
  for (int i=0;i<N;i++) {
      cout << abs(avg - score.at(i)) << endl;
  }
}