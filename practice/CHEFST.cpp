#include<bits/stdc++.h>
using namespace std;
int main(){
    long long t,n1,n2,m,mn,sum,d;
    scanf("%lld",&t);
    while(t--){
        scanf("%lld%lld%lld", &n1, &n2, &m);
        mn=min(n1,n2);
        d=max(n1,n2)-min(n1,n2);
        sum=max((long long)0,2*(mn-(m*(m+1))/2));
        printf("%lld\n",sum+d);
    }
}