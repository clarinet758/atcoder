#include<bits/stdc++.h>
using namespace std;

int main(){
    int r,c,k,ans=0;
    scanf("%d %d %d",&r,&c,&k);
    int b[r][c][2];
    char s[r][c];
    for (int i=0;i<r;i++) for (int j=0;j<c;j++) {
        b[i][j][0]=0;
        b[i][j][1]=0;
    }
    for (int i=0;i<r;i++) {
        scanf("%s",s[i]);
    }
    for (int i=0;i<r;i++) for (int j=0;j<c;j++) {
        if (i==0) {
            if (s[i][j]=='o') b[i][j][0]=1;
            if (s[r-i-1][j]=='o') b[r-i-1][j][1]=1;
        } else {
            if (s[i][j]=='o') b[i][j][0]=b[i-1][j][0]+1;
            if (s[r-i-1][j]=='o') b[r-i-1][j][1]=b[r-i][j][1]+1;
        }
    }
    for (int i=k-1;i<r-(k-1);i++) for (int j=k-1;j<c-(k-1);j++) {
        bool f[2]={1,1};
        for (int p=0;p<k;p++) {
            if (b[i][j+p][0]<k-p || b[i][j+p][1]<k-p) f[0]=0;
            if (b[i][j-p][0]<k-p || b[i][j-p][1]<k-p) f[1]=0;
            }
        if (f[0]==f[1] && f[0]==true) {
            ans+=1;
        }
    }
    printf("%d\n",ans);
    return 0;
}
