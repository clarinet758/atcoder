#include<bits/stdc++.h>
using namespace std;
// https://qiita.com/nomikura/items/1518bc8a6e04d2580b0d
char a[5][5];
int b[5][5], c[5][5];

int calc() {
    int score=0;
    for (int i=0;i<2;i++) for (int j=0;j<3;j++) if (a[i][j]==a[i+1][j]) score+=b[i][j];
    for (int i=0;i<3;i++) for (int j=0;j<2;j++) if (a[i][j]==a[i][j+1]) score+=c[i][j];
    return score;
}

int dfs(int turn) {
    if (turn==9) return calc();
    if (turn%2==0) {
        int m=-1;
        for (int i=0;i<3;i++) for (int j=0;j<3;j++) {
            if (a[i][j] !='*') continue;
            a[i][j]='o';
            m=max(m, dfs(turn+1));
            a[i][j]='*';
        }
        return m;
    } else {
        int n=1e8;
        for (int i=0;i<3;i++) for (int j=0;j<3;j++) {
            if (a[i][j]!='*') continue;
            a[i][j]='x';
            n=min(n,dfs(turn +1));
            a[i][j]='*';
        }
        return n;
    }
}

int main(){
    int cnt=0;
    for (int i=0;i<2;i++) for (int j=0;j<3;j++) {
        cin>>b[i][j];
        cnt+=b[i][j];
    }
    for (int i=0;i<3;i++) for (int j=0;j<2;j++) {
        cin>>c[i][j];
        cnt+=c[i][j];
    }

    fill(a[0],a[5], '*');
    int cho=dfs(0);
    printf("%d\n",cho);
    printf("%d\n",cnt-cho);
    return 0;
}
