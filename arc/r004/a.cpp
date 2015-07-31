#include<bits/stdc++.h>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;


int main(){
    int N,x,y;
    double ans=-1.0;
    scanf("%d",&N);
    int lst[N][2]; 
    for(int i=0;i<N;i++){
        scanf("%d %d",&x,&y);
        lst[i][0]=x;
        lst[i][1]=y;
    }
    for(int i=0;i<N-1;i++){
        for(int j=i+1;j<N;j++){
            int x1=lst[j][1]-lst[i][1];
            int y1=lst[j][0]-lst[i][0];
            double tmp=sqrt(x1*x1+y1*y1);
            if(ans<tmp) ans=tmp;
        }
    }
    printf("%.10lf\n",ans);
    return 0;
}
