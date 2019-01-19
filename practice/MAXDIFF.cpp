#include<bits/stdc++.h>
using namespace std;
int main(){
    int t,n,k,tmp;
    vector <int> v;
    cin>>t;
    while(t--){
        scanf("%d%d", &n, &k);
        if(k>n/2) k=n-k;
        for(int i=0;i<n;i++){
            scanf("%d",&tmp);
            v.push_back(tmp);
        }
        sort(v.begin(),v.end());
        int sum=0,sumk=0;
        for(int i=0;i<v.size();i++){
            sum+=v[i];
            if(i<k)sumk+=v[i];
        }
        printf("%d\n",sum-2*sumk);
        v.clear();
    }
}