#include<bits/stdc++.h>

using namespace std;

int main(){
    int n,k,f=0,tmp,chk;
    bool b[10]={0};
    scanf("%d %d",&n,&k);
    vector<int> d(k);
    for(auto&e:d) scanf("%d",&e);
    for (int i=0;i<k;i++) b[d[i]]=1;
    for (int i=n;i<100000;i++) {
        f=0;
        tmp=i;
        while (tmp>0) {
            chk=tmp%10;
            tmp/=10; 
            if (b[chk]==1) {
                f=1;
                break;
            }
        }
        if (f==0 && i>=n) {
            printf("%d\n",i);
            break;
        }
    }
    return 0;
}
