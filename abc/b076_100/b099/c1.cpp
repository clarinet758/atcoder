#include<bits/stdc++.h>
using namespace std;

int main(){
    int n,tmp;
    scanf("%d",&n);
    int d[100001];
    bool x[100001];
    for (int i=0;i<100001;i++) x[i]=0;
    d[0]=1;
    int t[12]={1,6,9,36,81,216,729,1296,6561,7776,46656,59049};
    for (int i=1;i<100001;i++) {
        for (int j=0;j<12;j++) {
            tmp=i+t[j]-1;
            if (tmp>100000) break;
            if (x[tmp]==0) {
                d[tmp]=d[i-1]+1;
                x[tmp]=1;
            } else {
                d[tmp]=min(d[tmp],d[i-1]+1);
            }
        }
    }
    printf("%d\n",d[n]-1);        
    return 0;
}
