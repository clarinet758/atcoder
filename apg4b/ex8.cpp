#include <bits/stdc++.h>
using namespace std;
 
int main() {
  int p;
  char text[1001];
  int price;
  scanf("%d",&p);
  if (p==1) {
      scanf("%d",&price);
  }
  if (p==2) {
      scanf("%s",text);
      scanf("%d",&price);
      printf("%s!\n",text); 
  }
  int n;
  scanf("%d",&n);
  printf("%d\n",price*n); 
  return 0;
}
