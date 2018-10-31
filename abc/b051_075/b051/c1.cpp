#include<bits/stdc++.h>
using namespace std;


int ul(int x,int y,int f){
    char w[4] = {'R', 'U', 'L', 'D'};
    for (int i=0;i<x;i++) printf("%c",w[f%2*2]);
    for (int i=0;i<y;i++) printf("%c",w[f%2*2+1]);
    return 0;
}

int main(){
    int sx,sy,tx,ty;
    scanf("%d %d %d %d",&sx,&sy,&tx,&ty);
    ul(abs(sx-tx),abs(sy-ty),0);
    ul(abs(sx-tx),abs(sy-ty),1);
    printf("D");
    ul(abs(sx-tx)+1,abs(sy-ty)+1,0);
    printf("LU");
    ul(abs(sx-tx)+1,abs(sy-ty)+1,1);
    printf("R\n");
    return 0;
}
