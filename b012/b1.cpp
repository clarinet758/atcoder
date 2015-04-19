#include<iostream>
#include<cmath>
#include<string>
#include<cctype>
#include<vector>
#include<numeric>
#include<algorithm>
using namespace std;
/**
vector<int>ar(3);
for(auto&e:ar){
    scanf("%d",&e);
	}
sort(ar.begin(),ar.end())
int sum=accumulate(ar.begin(),ar.end(),0);
**/

int main(){
    double pai=3.141592653589;
    int n;
    scanf("%d",&n);
    printf("%02d:%02d:%02d\n",n/3600,(n%3600)/60,n%60);
}
