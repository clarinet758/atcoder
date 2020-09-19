#include<bits/stdc++.h>
using namespace std;

int main(){
    char c[1005];
    
    scanf("%s",c);
    printf("%s",c);
    printf("%s\n",c[strlen(c)-1]=='s'?"es":"s");
    return 0;
}
