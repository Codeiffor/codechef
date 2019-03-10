#include<bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin>>t;
    int n;
    while(t--){
        scanf("%d", &n);
        int x;
        int cp=0, cz=0, cn=0;
        for(int i = 0; i < n; i++){
            scanf("%d", &x);
            if(x>0)
                cp++;
            else
                cn++;
        }
        if(cp>=cn){
            if(cn==0)
                cn=cp;
            printf("%d %d\n", cp, cn);
        }
        else{
            if(cp==0)
                cp=cn;
            printf("%d %d\n", cn, cp);
        }
    }
}