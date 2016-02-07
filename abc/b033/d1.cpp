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

int dis(int x1,int y1,int x2,int y2){
    return ((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));

}
int main(){
    double pai=3.141592653589;
    int n;
    int ei=0,tyo=0,don=0;
    vector<pair<int,int>> l;
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        int a,b;
        scanf("%d %d",&a,&b);
        l.push_back(make_pair(a,b));
    }
    for(int i=0;i<n-2;i++){
        for(int j=i+1;j<n-1;j++){
            int t0=dis(l[i].first,l[i].second,l[j].first,l[j].second);
            for(int k=j+1;k<n;k++){
                vector<int> t(3);
                t[0]=t0;
                t[1]=dis(l[i].first,l[i].second,l[k].first,l[k].second);
                t[2]=dis(l[k].first,l[k].second,l[j].first,l[j].second);
                sort(t.begin(),t.end());
                if(t[0]+t[1]==t[2]){
                    tyo++;
                }else if(t[0]+t[1]<t[2]){
                    don++;
                }else{
                    ei++;
                }
            }
        }
    }
    printf("%d %d %d\n",ei,tyo,don);
    return 0;
}


