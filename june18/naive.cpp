#include<bits/stdc++.h>
using namespace std;
int main(){
    int t;
    scanf("%d",&t);
    int n,a,b,x,y;
    while(t--){
        scanf("%d%d%d",&n,&a,&b);
        vector<int> v;
        for(int i=0;i<n;i++){
            scanf("%d",&x);
            v.push_back(x);
        }
        x=0;y=0;
        for(vector<int>::iterator it=v.begin();it!=v.end();++it){
            if(*it==a)x++;
            if(*it==b)y++;
        }
        double p=(x*y)/double(n*n);
        printf("%lf\n",p);
        v.clear();
    }
    return 0;
}
