#include <bits/stdc++.h>
using namespace std;

int main() {
  
 // vector<vector<vector<int>>> w(3, vector<vector<int>>(2,vector<int>(3)));
 // for (int i=0;i<3;i++) for (int j=0;j<2;j++) for (int k=0;k<3;k++) cin >> w.at(i).at(j).at(k);
//  for (int i=0;i<3;i++) for (int j=0;j<2;j++) for (int k=0;k<3;k++) cout<<w.at(i).at(j).at(k);
//  puts("");


//  return 0;
  int N, M;
  cin >> N >> M;
  vector<int> A(M), B(M);
  for (int i = 0; i < M; i++) {
    cin >> A.at(i) >> B.at(i);
  }

  // ここにプログラムを追記
  // (ここで"試合結果の表"の2次元配列を宣言)
  vector <vector <int>> w(N, vector <int> (N,0));
  for (int i=0; i<M; i++) {
    w.at(A.at(i)-1).at(B.at(i)-1) = 1;
    w.at(B.at(i)-1).at(A.at(i)-1) = 2;
  }
  for (int i = 0; i < N; i++) for (int j = 0; j < N; j++) {
    if (j+1 < N) {
      if (w.at(i).at(j) == 0) cout << "- ";
      if (w.at(i).at(j) == 1) cout << "o ";
      if (w.at(i).at(j) == 2) cout << "x ";
    } else {
      if (w.at(i).at(j) == 0) cout << "-" << endl;
      if (w.at(i).at(j) == 1) cout << "o" << endl;
      if (w.at(i).at(j) == 2) cout << "x" << endl;
      
    }
  }
}
