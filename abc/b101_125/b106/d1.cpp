#include<bits/stdc++.h>
using namespace std;
//https://atcoder.jp/contests/abc106/submissions/3027852

int n,m,q,l[200009],r[200009], x[509][509], c[509][509];

int main(){
    scanf("%d %d %d",&n,&m,&q);
    for (int i=1;i<=m;i++) {
        scanf("%d %d",&l[i],&r[i]);
        x[l[i]][r[i]]++;
    }
    for (int i=1;i<=n;i++) for (int j=1;j<=n;j++) c[i][j]=c[i][j-1]+x[i][j];
    for (int i=1;i<=q;i++) {
        int a,b,sum=0;
        scanf("%d %d",&a,&b);
        for (int j=a;j<=b;j++) sum+=c[j][b]-c[j][a-1];
        printf("%d\n",sum);
    }
    return 0;
}
