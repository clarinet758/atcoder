#include <bits/stdc++.h>
using namespace std;
 
int main() {
  int N, M;
  cin >> N >> M;
  vector<int> A(M), B(M);
  for (int i = 0; i < M; i++) {
    cin >> A.at(i) >> B.at(i);
  }
  //cout << A.at(0) << B.at(0) << endl;
  //if (1) return 0;
  // (ここで"試合結果の表"の2次元配列を宣言)
  vector< vector<int> > data(N, vector<int> (N) );
  for (int i=0;i<M;i++) {
    data.at(A.at(i)-1).at(B.at(i)-1) = 1;
    data.at(B.at(i)-1).at(A.at(i)-1) = 2;
  }
  for (int i=0;i<N;i++) {
    for (int j=0;j<N;j++) {
      if (j<N-1) {
        if ((data.at(i).at(j)) == 1) cout << "o " ;
        if ((data.at(i).at(j)) == 2) cout << "x " ;
        if ((data.at(i).at(j)) == 0) cout << "- " ;
      } else {
        if ((data.at(i).at(j)) == 1) cout << "o" << endl;
        if ((data.at(i).at(j)) == 2) cout << "x" << endl;
        if ((data.at(i).at(j)) == 0) cout << "-" << endl;

      }
    }
  }
}