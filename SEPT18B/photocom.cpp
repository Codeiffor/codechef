#include<bits/stdc++.h>
using namespace std;
long long int gcd(long long int u,long long int v){
    while(v!=0){
        long long int r=u%v;
        u=v;
        v=r;
    }
    return u;
}
int main(){
    int t;
    cin>>t;
    long long int h1,w1,h2,w2,c,hlcm,wlcm,dh1,dh2,dw1,dw2,ch1,ch2,cw1,pcw2,pch1,pch2,pcw1,cw2,hx,hy,wx,wy;
    string hw1,hw2;
    hw1.reserve(1000000);
    hw2.reserve(1000000);
    while(t--){
        scanf("%lld%lld\n",&h1,&w1);
        getline(cin,hw1);
        scanf("%lld%lld\n",&h2,&w2);
        getline(cin,hw2);
        c=0;
        hlcm=(h1*h2)/gcd(h1,h2);
        wlcm=(w1*w2)/gcd(w1,w2);
        dh1=hlcm/h2;
        dh2=hlcm/h1;
        dw1=wlcm/w2;
        dw2=wlcm/w1;
        ch1=0,ch2=0;
        hx=0;hy=0;
        pch1=0;pch2=0;
        //h
        while(true){
            pch1=ch1;
            pch2=ch2;
            if(dh1*(ch1+1)==dh2*(ch2+1)){
                ch1++;
                ch2++;
                hx=hy;
                hy=dh1*ch1;
            }
            else if(dh1*(ch1+1)<dh2*(ch2+1)){
                ch1++;
                hx=hy;
                hy=dh1*ch1;
            }
            else{
                ch2++;
                hx=hy;
                hy=dh2*ch2;
            }
            if(hy>hlcm)break;
            //w
            wx=0;wy=0;cw1=0;cw2=0;pcw1=0;pcw2=0;
            while(true){
                pcw1=cw1;
                pcw2=cw2;
                if(dw1*(cw1+1)==dw2*(cw2+1)){
                    cw1++;
                    cw2++;
                    wx=wy;
                    wy=dw1*cw1;
                }
                else if(dw1*(cw1+1)<dw2*(cw2+1)){
                    cw1++;
                    wx=wy;
                    wy=dw1*cw1;
                }
                else{
                    cw2++;
                    wx=wy;
                    wy=dw2*cw2;
                }
                if(wy>wlcm)break;
                if(hw2[pch1*w2+pcw1]==hw1[pch2*w1+pcw2]){
                    c+=(hy-hx)*(wy-wx);
                }
            }
        }
        printf("%lld\n",c);
    }
    return 0;
}