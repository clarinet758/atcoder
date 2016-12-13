#include<bits/stdc++.h>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;


int main(){
// #109801 写経
    int N;
    bool used[1500] = {0}; //bool配列を24時間 x 60分より大きく, 初期値は全て0で用意

    scanf("%d",&N);
    for (int i=0;i<N;i++) {
       int s,e; //降り始め時間をstart 降り終わり時間をend
       
       //時間は60をかけて分のみにして処理
       //降り始めと降り終わりの%5の丸めが異なる
       scanf("%d-%d",&s,&e);
       int ss=(s/100)*60 + (s%100);
       ss-=(ss%5);
       int ee=(e/100)*60 + (e%100);
       ee+=(5-(ee%5))%5;

       //雨降りの時間の範囲をtrueにする
       for (int j=ss;j<=ee;j++) {
           used[j]=true;
       }
    }

    for (int i=0;i<=24*60;i++) {
        //00時00分からか、それ以降の時間でiがtrueで、i-1がfalseの時間を降り始めとする
        if ((i==0 && used[i]) || (used[i] && !used[i-1])) {
            int h=i/60, m=i%60;
            printf("%02d%02d-",h,m);
        }
        if ((i==24*60 && used[i]) || (used[i] && !used[i+1])) {
            int h=i/60, m=i%60;
            printf("%02d%02d\n",h,m);
        }
    }
    return 0;
}
