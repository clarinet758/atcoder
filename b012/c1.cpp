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
    for(int i=1;i<10;i++){
        for(int j=1;j<10;j++){
            if(i*j==2025-n){
                printf("%d x %d\n",i,j);
            }
        }
    }
    return 0;
}
