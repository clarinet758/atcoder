#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)

int n,ans,mod=1000000007;
char x[105];
void dfs (int p,int q){
    printf("%c %c %c  %d\n",x[0],x[1],x[2],q);
    if (p==q) {ans++; ans%=mod; return;}
    x[0]=x[1];
    x[1]=x[2];
    x[2]='A';
    if ((x[0]=='A' && x[1]=='G' && x[2]=='C') || (x[0]=='G' && x[1]=='A' && x[2]=='C') || (x[0]=='A' && x[1]=='C' && x[2]=='G')) {
        return;
    } else {
        dfs(p,q+1);
    }
    x[2]='C';
    if ((x[0]=='A' && x[1]=='G' && x[2]=='C') || (x[0]=='G' && x[1]=='A' && x[2]=='C') || (x[0]=='A' && x[1]=='C' && x[2]=='G')) {
        return;
    } else {
        dfs(p,q+1);
    }
    x[2]='G';
    if ((x[0]=='A' && x[1]=='G' && x[2]=='C') || (x[0]=='G' && x[1]=='A' && x[2]=='C') || (x[0]=='A' && x[1]=='C' && x[2]=='G')) {
        return;
    } else {
        dfs(p,q+1);
    }
    x[2]='T';
    dfs(p,q+1);
}

int main(){
    sc1(n);
    dfs(n,0);
    printf("%d\n",ans);
    return 0;
}
