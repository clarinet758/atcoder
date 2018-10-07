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
    int n,a,b,t,ans=0;
    scanf("%d %d %d",&n,&a,&b);
    for (int i=1;i<=n;i++) {
        t=i/10000+i%10000/1000+i%1000/100+i%100/10+i%10;
//        printf("%d ",t);
        if (a<=t && b>=t) ans+=i;
    }
    printf("%d\n",ans);

    return 0;
}

