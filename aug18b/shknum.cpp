#include<bits/stdc++.h>
using namespace std;
int main(){
    int t,i,n;
    cin>>t;
    int two[31];
    for(i=0;i<=30;i++){
        two[i]=pow(2,i);
    }
    int c,c1,c11,c12,c2;//,c21,c22;
    while(t--){
        cin>>n;
        for(i=0;i<=30;i++){
          if(two[i]>n){
              c2=two[i];
              break;
          }
          c1=two[i];
        }
        if(n==1){
            cout<<"2\n";
            continue;
        }
        if(c1==n){
            cout<<"1\n";
            continue;
        }
        for(i=0;i<=30;i++){
          if(two[i]==c1)continue;
          if(two[i]>n-c1){
              c12=two[i];
              break;
          }
          c11=two[i];
        }
        // for(i=0;i<=30;i++){
        //   if(two[i]==c2)continue;
        //   if(two[i]>c2-n){
        //       c22=two[i];
        //       break;
        //   }
        //   c21=two[i];
        // }
        // cout<<min(n-(c1+c11),min((c1+c12)-n,min(n-(c2-c22),(c2-c21)-n)))<<endl;
        cout<<min(n-(c1+c11),min((c1+c12)-n,c2+1-n))<<endl;
    }
    return 0;
}