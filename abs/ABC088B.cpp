#include<bits/stdc++.h>
#include<vector>

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
    int n,ans=0,f=0;
    scanf("%d",&n);
    vector<int>ar(n);
    for(auto&e:ar){
        scanf("%d",&e);
    }
    sort(ar.begin(),ar.end());
    for (int i=n-1;i>=0;i--) {
        if (f%2) {
            ans-=ar[i];
            f=0;
        } else {
            ans+=ar[i];
            f=1;
        }
    }
    printf("%d\n",ans); 
    return 0;
}

