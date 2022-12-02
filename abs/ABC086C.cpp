#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)
#define sc3(a,b,c)  scanf("%d %d %d",&a,&b,&c)

int main(){
    int n,t=0,x=0,y=0;
    sc1(n);
    rep(i,n){
        int a,b,c,p;
        sc3(a,b,c);
        p=abs(x-b)+abs(y-c);
        if(p>a-t || p%2!=(a-t)%2) { 
            cout << "No" << endl;
            return 0;
        }
        x=b,y=c,t=a;
    }
    cout << "Yes" << endl;
    return 0;
}
