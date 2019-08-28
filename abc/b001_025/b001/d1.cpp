#include<bits/stdc++.h>
using namespace std;

int main(){
    int n,p=0;
    int w[1450];
    for (int i=0;i<1450;i++) w[i]=0;
    scanf("%d",&n);
    for (int i=0;i<n;i++) {
        int a,b,s,g; 
        scanf("%d-%d",&a,&b);
        s=a/100*60+a%100;
        g=b/100*60+b%100;
        s-=s%5;
        g=g+(g%5>0?5-g%5:0);
        w[s]+=1;
        w[g]-=1;
    }
    for(int i=0;i<1450;i++) {
        if(p==0 && w[i]>0) {
            printf("%04d-",i/60*100+i%60);
        } else if(p>0 && p+w[i]==0) {
            printf("%04d\n",i/60*100+i%60);
        }
        p+=w[i];
    }
    return 0;
}
