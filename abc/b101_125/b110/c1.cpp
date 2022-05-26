#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)

char s[200005],t[200005];
int a[30],b[30];

int main(){
    scanf("%s",s);
    scanf("%s",t);
    long p=strlen(s);
    for (long i=0l;i<p;i++){
        a[s[i]-'a']++;
        b[t[i]-'a']++;
    }
    vector <int> c,d;
    rep(i,27){
        if(a[i]>0) c.push_back(a[i]);
        if(b[i]>0) d.push_back(b[i]);
    }
    sort(c.begin(),c.end());
    sort(d.begin(),d.end());
    int x=1;
    if (c.size()!=d.size()) {
        x=0;
    } else {
        for (int i=0;i!=c.size();i++) if (c[i]!=d[i]) x=0;
    }
    printf("%s\n",(x==1)?"Yes":"No");
    return 0;
}
