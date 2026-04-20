#include <bits/stdc++.h>
using namespace std;
//20260421
int main() {
  int N, M;
  cin >> N >> M;
  vector<int> A(M), B(M);
  for (int i = 0; i < M; i++) {
    cin >> A.at(i) >> B.at(i);
  }

  // ここにプログラムを追記
  // (ここで"試合結果の表"の2次元配列を宣言)
  vector<vector <int>> res(N, vector<int>(N,2));
  for(int i=0;i<M;i++){
    res.at(A.at(i)-1).at(B.at(i)-1)=1;
    res.at(B.at(i)-1).at(A.at(i)-1)=0;
  }
  for(int i=0;i<N;i++){
    for(int j=0;j<N;j++){
      if(res.at(i).at(j)==0) cout << "x";
      else if(res.at(i).at(j)==1) cout << "o";
      else cout << "-";
      if (j<N-1) cout << " ";
      else cout << endl;
    }
  }
}