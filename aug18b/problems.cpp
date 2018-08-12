#include<bits/stdc++.h>
using namespace std;
bool sortfirst(const pair<int,int>&a,const pair<int,int>&b){
    return(a.first<b.first);
}
int main(){
    int p,s,i,j;
    cin>>p>>s;
    int sc[s];
    int ns[s];
    int n;
    vector <pair <int,int> > problem;
    vector <pair <int,int> > difficulty;
    for(i=0;i<p;i++){
        n=0;
        for(j=0;j<s;j++)
            scanf("%d",&sc[j]);
        for(j=0;j<s;j++)
            scanf("%d",&ns[j]);
        for(j=0;j<s;j++)
            problem.push_back(make_pair(sc[j],ns[j]));
        sort(problem.begin(),problem.end(),sortfirst);
        for(j=0;j<s-1;j++)
            if(problem[j].second>problem[j+1].second)
                n++;
        problem.clear();
        difficulty.push_back(make_pair(n,i));
    }
    sort(difficulty.begin(),difficulty.end());
    for(i=0;i<p;i++)
        cout<<difficulty[i].second+1<<endl;
    return 0;
}