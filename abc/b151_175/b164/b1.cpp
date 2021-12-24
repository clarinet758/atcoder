#include<bits/stdc++.h>
using namespace std;

int main(){
    int a,b,c,d;
    cin >> a >> b >> c >> d;
    printf("%s\n",((c/b+(c%b>0))>(a/d+(a%d>0)))?"No":"Yes");
    return 0;
}
