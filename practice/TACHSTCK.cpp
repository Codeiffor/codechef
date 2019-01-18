#include<bits/stdc++.h>
using namespace std;
int main(){
    int n,d;
    scanf("%d%d",&n,&d);
    int a[n];
    for(int i;i<n;i++)
        scanf("%d", &a[i]);
    sort(a,a+n);
    int count=0;
    for (int i=0;i<n-1;i++){
        if(a[i+1]-a[i]<=d){
            ++i;
            count++;
        }
    }
    printf("%d",count);
}