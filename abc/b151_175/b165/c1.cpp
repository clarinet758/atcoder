#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)
#define sc2(a,b)  scanf("%d %d",&a,&b)
#define sc3(a,b,c)  scanf("%d %d %d",&a,&b,&c)

int main(){
    int n,m,q;
    long long ans=0ll;
    sc3(n,m,q);
    vector <vector<int>> w(q,vector <int> (4));
    vector <int> dd(10);
    rep(i,q) cin >> w.at(i).at(0) >> w.at(i).at(1) >> w.at(i).at(2) >> w.at(i).at(3);
    for (int a=1;a<11;a++) {
        dd.at(0)=a;
        for (int b=a;b<11;b++) {
            dd.at(1)=b;
            for (int c=b;c<11;c++) {
                dd.at(2)=c;
                for (int d=c;d<11;d++) {
                    dd.at(3)=d;
                    for (int e=d;e<11;e++) {
                        dd.at(4)=e;
                        for (int f=e;f<11;f++) {
                            dd.at(5)=f;
                            for (int g=f;g<11;g++) {
                                dd.at(6)=g;
                                for (int h=g;h<11;h++) {
                                    dd.at(7)=h;
                                    for (int i=h;i<11;i++) {
                                        dd.at(8)=i;
                                        for (int j=i;j<11;j++) {
                                            dd.at(9)=j;
                                            long long tmp=0ll;
                                            rep(x,q) if (dd.at(w.at(x).at(1)-1) - dd.at(w.at(x).at(0)-1) == w.at(x).at(2) && dd.at(w.at(x).at(1)-1)<=m) tmp+=w.at(x).at(3);
                                            ans=max(ans,tmp);
                                            
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    printf("%lld\n",ans);
    return 0;
}
