#include<bits/stdc++.h>
using namespace std;

int main(){
    double l,p;
    cin >> l;
    p=l/3.0;
    printf("%.15lf\n",p*p*(l-p-p));
    return 0;
}
