#include <bits/stdc++.h>
using namespace std;
//20260419
int main() {
  int N, A;
  cin >> N >> A;

  // ここにプログラムを追記
  string op;
  int B;
  for (int i=0;i<N;i++){
    cin >> op >> B;
    if (op=="/" && B==0){
      cout << "error" << endl;
      break;
    } else {
        if(op=="+"){
            A+=B;
        } else if(op=="-"){
            A-=B;
        } else if(op=="*"){
            A*=B;
        } else {
            A/=B;
        } 
        cout << i + 1 << ":" << A << endl;
    }
  }
}