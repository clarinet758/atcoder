#include<bits/stdc++.h>

using namespace std;

int main(){
    char s1[101],s2[100],s3[100];
    deque<char> a;
    deque<char> b;
    deque<char> c;
    scanf("%s",s1);
    for (int i=0;i<strlen(s1);i++) a.push_back(s1[i]);
    scanf("%s",s2);
    for (int i=0;i<strlen(s2);i++) b.push_back(s2[i]);
    scanf("%s",s3);
    for (int i=0;i<strlen(s3);i++) c.push_back(s3[i]);
    int f=0;
    for(;;) {
        if (f==0) {
            if (a.empty()) {
                printf("A\n");
                break;
            }
            f=a.front()-'a';
            a.pop_front();
        } else if (f==1) {
            if (b.empty()) {
                printf("B\n");
                break;
            }
            f=b.front()-'a';
            b.pop_front();
        } else {
            if (c.empty()) {
                printf("C\n");
                break;
            }
            f=c.front()-'a';
            c.pop_front();
        }
    }
    return 0;
}
