#include<bits/stdc++.h>
using namespace std;

// from https://utpc2014.contest.atcoder.jp/submissions/1015041
typedef long long ll;
typedef pair<int,int> pii;
#define rep(i,n) for(ll i=0;i<(ll)(n);i++)
#define all(a)  (a).begin(),(a).end()
#define pb push_back
#define INF (1e9+1)

#define MAX_V 100000
vector<int> G[MAX_V];

void visit(int cur,int prev,vector<pii> &brg,vector<vector<int>> &each_bcc,vector<int> &cmp,stack<int> &roots,stack<int> &S, vector<bool> &inS, vector<int> &order, int &k){
    order[cur]=++k;
    S.push(cur); inS[cur]=true;
    roots.push(cur);

    rep(i,G[cur].size()){
        int to=G[cur][i];
        if(order[to]==0){
            visit(to,cur,brg,each_bcc,cmp,roots,S,inS,order,k);
        } else if(to!=prev && inS[to]){
            while(order[roots.top()]>order[to]) roots.pop();
        }
    }

    if(cur==roots.top()){
        if(prev!=-1)brg.pb(pii(prev,cur));
        vector<int> bcc;
        while(1){
            int node=S.top(); S.pop(); inS[node]=false;
            bcc.pb(node);
            cmp[node]=each_bcc.size();
            if(node==cur)break;
        }
        each_bcc.pb(bcc);
        roots.pop();
    }
}

void bridge(int V,vector<pii> &brg,vector<vector<int>> &each_bcc,vector<int> &cmp) {
    vector<int> order(V);
    vector<bool> inS(V);
    stack<int> roots,S;
    int k=0;
    rep(i,V) if(order[i]==0) visit(i,-1,brg,each_bcc,cmp,roots,S,inS,order,k);
}
    

int main(){
    int n;
    scanf("%d",&n);
    rep(i,n){
        int a,b;
        scanf("%d %d",&a,&b);
        a--,b--;
        G[a].pb(b);
        G[b].pb(a);
    }
    vector<pii> brg;
    vector<vector<int>> each_bcc;
    vector<int> cmp(n);
    bridge(n,brg,each_bcc,cmp);

    int circle_size=0;
    rep(i,each_bcc.size()) circle_size=max<int> (circle_size,each_bcc[i].size());

    if(circle_size%2!=0) n--;
    //if (each_bcc.size()>1) printf("1 %d\n",n);
    //else printf("2 %d\n",n);
    printf("%d\n",circle_size);
    return 0;
}
