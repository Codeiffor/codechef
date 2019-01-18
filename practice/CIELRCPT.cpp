#include<bits/stdc++.h>
using namespace std;
int main(){
    int t,n;
    scanf("%d",&t);
    while(t--){
        scanf("%d",&n);
        int count=0;
        for(int i=11; i>=0;i--){
            do{
                if(n>=pow(2,i)){
                    n-=pow(2,i);
                    count++;
                }
                else break;
            }while(i==11);
        }
        printf("%d\n",count);
    }
}