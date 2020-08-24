#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc2(a,b)  scanf("%d %d",&a,&b)

const int dx[]={-1,0,1,0}, dy[]={0,-1,0,1};
int h,w,sx,sy,gx,gy;
char m[505][505];
bool dfs(int y,int x) {
    if (m[y][x]=='#') return 0;
    if (y==gy && x==gx) return 1;
    m[y][x]='#';
    bool ret=0;
    rep(i,4) {
        int ny=y+dy[i];int nx=x+dx[i];
        if (ny<0 || ny>=h || nx<0 || nx>=w) continue;
        ret|=dfs(ny,nx);
    }
    return ret;
}

int main(){
    sc2(h,w);
    rep(i,h)  scanf("%s",m[i]);
    rep(i,h) rep(j,w) {
        if (m[i][j]=='s') {sx=j;sy=i;}
        if (m[i][j]=='g') {gx=j;gy=i;}
    }
    if(dfs(sy,sx)) puts("Yes");
    else puts("No");
    return 0;
}
