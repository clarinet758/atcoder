#include<bits/stdc++.h>

using namespace std;

#define PI 3.1415926535897932

//typedef long long ll;


int lcm(int a,int b) { return a*b/__gcd(a,b); }
//ll lcm(ll a,ll b) { return a*b/__gcd(a,b); }

/**
 * vector<int>ar(3);
 * for(auto&e:ar){
 *     scanf("%d",&e);
 * }
 * sort(ar.begin(),ar.end())
 * int sum=accumulate(ar.begin(),ar.end(),0);
 **/


int main(){
    int mod=1000000007;
    int n,y;
    scanf("%d %d",&n,&y);
    int a=0,b=n,c=0;
    for (int i=0;i<n;i++) {
        if (a*10000+b*5000+c*1000>y) {
            b-=1;
            c+=1;
        } else if (a*10000+b*5000+c*1000<y) {
            b-=1;
            a+=1;
        }
    }
    if (a*10000+b*5000+c*1000==y) {
        printf("%d %d %d\n",a,b,c);
    } else {
        printf("-1 -1 -1\n");
    }

    return 0;
}

