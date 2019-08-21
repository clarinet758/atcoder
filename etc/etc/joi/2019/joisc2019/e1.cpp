#include<bits/stdc++.h>
using namespace std;

int main(){
    int n,m;
    scanf("%d %d",&n,&m);
    vector<long long> A(n), B(m), S(n), T(m), P(n), Q(m);
    for (int i=0;i<n;i++) {
        long long a,s,p;
        scanf("%lld %lld %lld",&a,&s,&p);
        A[i]=a;S[i]=s;P[i]=p;
    }

    for (int i=0;i<m;i++) {
        long long b,t,q;
        scanf("%lld %lld %lld",&b,&t,&q);
        B[i]=b;T[i]=t;Q[i]=q;
    }
    long long ans=0,sum=0;
    vector<long long>asum(n);
    vector<pair<long long,pair<int, long long>>> margin;
    for(int i=0;i<n;i++) {
        sum+=A[i];
        asum[i]=sum;
        if (sum<=S[i]) {
            ans+=P[i];
            margin.push_back(make_pair(S[i]-sum,make_pair(i,P[i])));
        }
    }
    sort(margin.begin(),margin.end());
    map<int, long long> mp;
    sum=0;
    int pos=0;
    for (int i=0;i<m;i++) {
        sum+=B[i];
        vector<pair<int, long long>> v;
        while(pos<(int)margin.size() && margin[pos].first<sum) {
            v.push_back(margin[pos].second);
            pos++;
        }
        if(sum<=T[i]) {
            int p=upper_bound(asum.begin(), asum.end(),T[i]-sum)-asum.begin();
            if (p<n) {
                v.push_back(make_pair(p,-Q[i]));
            } else {
                ans+=Q[i];
            }
        }
        sort(v.begin(), v.end());
        for (int j=(int)v.size()-1;j>=0;j--) {
            if (v[j].second>0) {
                mp[v[j].first]+=v[j].second;
            } else if (v[j].second<0) {
                auto it=mp.lower_bound(v[j].first);
                long long rem=-v[j].second;
                while (rem>0&& it!= mp.end()) {
                    if(rem<it->second) {
                        it->second-=rem;
                        rem=0;
                    } else {
                        rem-=it->second;
                        it=mp.erase(it);
                    }
                }
                ans+=rem;
            }
        }
    }
    printf("%lld\n",ans);
        
    return 0;
}
