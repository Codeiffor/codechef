#include<bits/stdc++.h>
using namespace std;
int arr[100001];
int t,n,k;
int mx=100100;

int cmp(int a, int b, int c, int d){
    int x[mx];
    for(int i=0;i<mx;i++)
        x[i]=0;
    for(int i=a;i<=b;i++){
        x[arr[i]]++;
    }
    for(int i=0;i<mx-1;i++){
        x[i+1]+=x[i]/k;
        x[i]%=k;
    }

    int y[mx];
    for(int i=0;i<mx;i++)
        y[i]=0;
    for(int i=c;i<=d;i++){
        y[arr[i]]++;
    }
    for(int i=0;i<mx-1;i++){
        y[i+1]+=y[i]/k;
        y[i]%=k;
    }

    for(int i=mx-1;i>=0;i--){
        if(x[i]<y[i])return -1;
        else if(x[i]>y[i])return 1;
    }
    return 0;
}
int main(){
    int i;
    scanf("%d",&t);
    while(t--){
        scanf("%d%d", &n, &k);
        for(i=0;i<n;i++)
            cin>>arr[i];
        int start=0,end=n-2,best=0;
        while(start<=end){
            int mid=(start+end)/2;
            if(cmp(0,mid,mid+1,n-1)==-1){
                best=mid;
                start=mid+1;
            }
            else
                end=mid-1;
        }
        if(best!=n-2){
        if(cmp(0,best+1,best+2,n-1)==0)best++;
        else if(cmp(0,best,best+2,n-1)==-1)best++;
        }
        printf("%d\n",best+1);
    }
}