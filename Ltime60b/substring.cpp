#include<bits/stdc++.h>
using namespace std;
int main(){
  int t,k,i,j,x,count,n,distinct_char,val;
  scanf("%d",&t);
  string s;
  int occ[26];
  bool cond;

  while(t--){
    cin>>s>>k;
    n=s.length();
    count=0;
    ///
    for(i=0;i<n;i++){
      for(x=0;x<26;x++)
        occ[x]=0;
      ///
      for(j=i;j<n;j++){
        occ[int(s[j])-97]++;
        distinct_char=0;
        val=0;
        cond=true;

        for(x=0;x<26;x++){
          if(occ[x]==0)continue;
          if(val>0){
            if(occ[x]!=val){
              cond=false;
              break;
            }
          }
          else{
            val=occ[x];
          }
          distinct_char++;
        }

        if(distinct_char<k)cond=false;
        if(cond==true)count++;
      }
      ///
    }
    ///
    printf("%d\n",count);
  }
  return 0;
}
