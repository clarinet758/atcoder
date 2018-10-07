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
    int n,d,ans=0;
    bool a[101]={0};

    scanf("%d",&n);
    for (int i=0;i<n;i++) {
        scanf("%d",&d);
        if (a[d]==0) ans++;
        a[d]=1;
    }
    printf("%d\n",ans); 

    return 0;
}

