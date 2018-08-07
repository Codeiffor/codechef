#include<bits/stdc++.h>
using namespace std;
int main(){
    int t,i;
    cin>>t;
    bool bob;
    string a,b;
    while(t--){
        cin>>a>>b;
        bob=true;
        for(i=0;i<3;i++)
            if(a[i]!='b'&& a[i]!='o'&& b[i]!='b'&& b[i]!='o')
                bob=false;
        if(bob){
            int bc=0,oc=0;
            for(i=0;i<3;i++){
                if(a[i]=='b'||b[i]=='b')bc++;
                if(a[i]=='o'||b[i]=='o')oc++;
            }
            if(bc<2||oc<1)bob=false;
        }
        cout<<(bob?"yes\n":"no\n");
    }
    return 0;
}