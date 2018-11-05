#include<bits/stdc++.h>
using namespace std;

int main(){
    char s[101];
    int f=0;
    vector<int> a(4);
    scanf("%s",s);
    for (auto&e:a)  scanf("%d",&e);

    for (int i=0;i<strlen(s);i++) {
        if (i==a[f]) {
            printf("\"%c",s[i]);
            if (f<3) f++;
        } else {
            printf("%c",s[i]);
        }
    }
    if (a[f]==strlen(s)) printf("\"");
    printf("\n");

    return 0;
}
