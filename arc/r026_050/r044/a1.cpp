#include<bits/stdc++.h>
using namespace std;

int main(){
    long n;
    scanf("%ld",&n);
    printf("%s\n",(n==1 || (n%2==0 && n!=2) || (n%3==0 && n!=3) || (n%5==0 && n!=5))?"Not Prime":"Prime");

    return 0;
}
