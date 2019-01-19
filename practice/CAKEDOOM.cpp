#include<bits/stdc++.h>
using namespace std;
bool isn(char c){
    return c!='?';
}
int main(){
    int t,k,l;
    string s;
    scanf("%d\n",&t);

    while(t--){
        scanf ("%d\n", &k);
        getline (cin, s);
        l = s.length();
        bool no = false;

        if(l==1){
            if(!isn(s[0]))
                s='0';
            cout<<s<<endl;
            continue;
        }

        for (int i=0; i<l; i++) {
            if( !isn (s[i]))
                continue;
            if(s[i]==s[(i-1+l)%l])
                no=true;
        }
        
        if(k==1) no=true;

        else if(k==2){
            for (int i=0; i<l; i++) {
                if(isn(s[i])){
                    if(i!=0){
                        if(( i%2==0 && s[i]=='0') || ( i%2==1 && s[i]=='1'))
                            s[0]='0';
                        else
                            s[0]='1';
                    }
                    break;
                }
                if(i==l-1)s[0]='0';
            }
            for (int i=1; i<l; i++){
                if(!isn(s[i])){
                    if(s[i-1]=='0')
                        s[i]='1';
                    else
                        s[i]='0';
                }
                if(s[i]==s[i-1])
                    no=true;
                if(i==l-1 && s[i]==s[0])
                    no=true;
            }
        }

        else{
            for (int i=0; i<l; i++){
                if(!isn(s[i])){
                    bool v0=false,v1=false;
                    if(s[(i-1+l)%l]=='0' || s[(i+1)%l]=='0')
                        v0=true;
                    if(s[(i-1+l)%l]=='1' || s[(i+1)%l]=='1')
                        v1=true;
                    if(v0 && v1)
                        s[i]='2';
                    else if(v0)
                        s[i]='1';
                    else
                        s[i]='0';
                }
            }
        }

        if(no){
            cout<<"NO"<<endl;
            continue;
        }

        cout<<s<<endl;
    }
    return 0;
}