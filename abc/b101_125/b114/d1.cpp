#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)

int cnt[105];
//10 1   /  100 543
int main(){
    int xod=100, n,m=0,ans=0;
    vector <int> pb;
    bool tb[xod+3];
    rep(i,xod+3) tb[i]=1;
    sc1(n);
    for(int i=2;i*i<=101;i++) {
        if (!tb[i]) continue;
        for(int j=i*i;j<=xod;j+=i) {
            tb[j]=0;
        }
    }
    for(int i=2;i<xod;i++) if(tb[i]) pb.push_back(i);
    for(auto i=pb.begin();i!=pb.end();++i) m++;
    for(int i=2;i<=n;i++) {
        int w=i;
        for (auto j=pb.begin();j!=pb.end();++j) {
            if(w==1) break;
            while(w%*j==0) {
                cnt[*j]++;
                w/=*j;
            }
        }
    }

    int ans2=0,ans3=0;
    for (int i=0;i<25;i++) for(int j=0;j<25;j++) for(int k=0;k<25;k++) {
        if (i!=j && i!=k && j!=k) {
            if (cnt[pb[i]]>3 && cnt[pb[j]]>3 && cnt[pb[k]]>3)  ans3++;
            else if (cnt[pb[i]]>1 && cnt[pb[j]]>3 && cnt[pb[k]]>3)  ans2++;
        }
    } 
    ans+=(ans2/2) + (ans3/2);
    int ans4=0; ans2=0;
    for (int i=0;i<25;i++) for(int j=0;j<25;j++) {
        if (i!=j) {
            if (cnt[pb[i]]>23 && cnt[pb[j]]>23 ) ans4++;
            else if (cnt[pb[i]]>3 && cnt[pb[j]]>23) { ans2++; ans2++; }
            else if (cnt[pb[i]]>3 && cnt[pb[j]]>13) ans2++;
            else if (cnt[pb[i]]>1 && cnt[pb[j]]>23) ans2++;
        }
    }
    ans+=(ans2) + (ans4*2);
    rep(i,100) if (cnt[i]>73) ans++;
    printf("%d\n",ans);
    return 0;
}
