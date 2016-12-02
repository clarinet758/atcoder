#include<bits/stdc++.h>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;


int main(){
    int mod=1000000007;
    int Deg,Dis;
    scanf("%d %d",&Deg,&Dis);
    char dir[][4] = {"N","NNE","NE","ENE","E","ESE","SE","SSE","S","SSW","SW","WSW","W","WNW","NW","NNW","C"};
    Deg=Deg*10+1125;
    if (Deg>=36000) Deg-=36000;
    
    if (Dis<15) Deg=16;
    else Deg=Deg/2250;
    
    int w;
    if (Dis<15) w=0;
    else if (Dis<93) w=1;
    else if (Dis<201) w=2;
    else if (Dis<327) w=3;
    else if (Dis<477) w=4;
    else if (Dis<645) w=5;
    else if (Dis<831) w=6;
    else if (Dis<1029) w=7;
    else if (Dis<1245) w=8;
    else if (Dis<1467) w=9;
    else if (Dis<1707) w=10;
    else if (Dis<1959) w=11;
    else w=12;

    printf("%s %d\n",dir[Deg],w);

    return 0;
}
