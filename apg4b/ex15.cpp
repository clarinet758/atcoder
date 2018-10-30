#include<bits/stdc++.h>

using namespace std;

int input(int n){
    vector<int> a(n);
    for (auto&e:a) scanf("%d",&e);
    return accumulate(a.begin(), a.end(), 0);
}

int output(int x,int y,int z) {
    printf("%lld\n",x*y*z);
    return 0;
}


int main(){
    int n;
    scanf("%d",&n);
    int x = input(n);
    int y = input(n);
    int z = input(n);
    output(x,y,z);

    return 0;
}
