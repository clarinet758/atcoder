#include<bits/stdc++.h>
using namespace std;

vector<string> news={"N","NNE","NE","ENE","E","ESE","SE","SSE","S","SSW","SW","WSW","W","WNW","NW","NNW","C"};
int main(){
    int g,s,t;
    scanf("%d %d",&g,&s);
    g=(g*10+1125)%36000;
    s=(s*10)/6;
    if (s<25) t=0;
    else if (s<155) t=1;
    else if (s<335) t=2;
    else if (s<545) t=3;
    else if (s<795) t=4;
    else if (s<1075) t=5;
    else if (s<1385) t=6;
    else if (s<1715) t=7;
    else if (s<2075) t=8;
    else if (s<2445) t=9;
    else if (s<2845) t=10;
    else if (s<3265) t=11;
    else t=12;
    if (t==0) g=37125;
    cout << news[g/2250] << " " << t << endl;
    return 0;
}
