#include<bits/stdc++.h>
using namespace std;
int main(){
  int t;
  scanf("%d",&t);
  int n,i,j;
  while(t--){
    scanf("%d",&n);
    int a[n][n];
    for(i=0;i<n;i++)
      for(j=0;j<n;j++)
        scanf("%d",&a[i][j]);
    int max=0;
    int temp1,temp2=0;
    for(i=0;i<n;i++){
      temp1=0;
      temp2=0;
      for(j=i;j<n;j++){
          temp1+=a[j][j-i];
          temp2+=a[j-i][j];
      }
      if(temp1>max)max=temp1;
      if(temp2>max)max=temp2;
    }
    printf("%d\n",max);
  }
  return 0;
}
