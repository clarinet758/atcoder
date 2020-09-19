#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define per(i,n)  for(int i=n-1;i>=0;--i)
#define sc1(a)  scanf("%d",&a)
#define sc3(a,b,c)  scanf("%d %d %d",&a,&b,&c)

int main(){
    map <int, int> x;
    int n,a,chk=0;
    sc1(n);
    rep(i,n) {
        sc1(a);
        if (i<2) {
            for (int j=1;j*j<=a;j++) {
                if (a%j==0) x[j]++;
                if (a%j==0 && j*j!=a) x[a/j]++;
            }
        }else{
            printf("%d\n",i);
            for (auto itr =x.begin();itr!=x.end();++itr) {
                int j = itr->first;
                //printf("%d\n",j);
                if (a%j==0) x[j]++;
                if (a%j==0 && j*j!=a) x[a/j]++;
            }

        }
    }

    int aa=0;
    for (auto itr =x.begin();itr!=x.end();++itr) {
        //printf("%d %d\n",itr->first,itr->second);
        if (itr->second >= n-1) aa=max(aa,itr->second);
    }
     printf("%d\n",aa);
    return 0;
}
