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
    int a,b,c,x,ans=0;
    scanf("%d",&a);
    scanf("%d",&b);
    scanf("%d",&c);
    scanf("%d",&x);
    for (int i=0;i<=a;i++){
        for (int j=0;j<=b;j++) {
            for (int k=0;k<=c;k++){
                if (x==i*500+j*100+k*50) ans++;
            }
        }
    }
    printf("%d\n",ans);

    return 0;
}

