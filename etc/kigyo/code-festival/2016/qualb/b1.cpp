#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc3(a,b,c)  scanf("%d %d %d",&a,&b,&c)

int main(){
    int n,a,b,m,ans;
    char s[100005];
    sc3(n,a,b);
    m=b;
    scanf("%s",s);
    rep (i,n) {
        if (s[i]=='a' && a+b>0) {
            printf("Yes\n");
            a--;
        } else  if (s[i]=='b' && a+b>0 && b>0) {
            printf("Yes\n");
            b--;
        } else {
            printf("No\n");
        }
    }
    return 0;
}
