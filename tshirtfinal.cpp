#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
 
string func(){
    string s1,s2;
    cin>>s1>>s2;
    char ch1 = s1.back();
    char ch2 = s2.back();
    if(s1==s2){
        return "=";
    }
    else if((s1=="M" && s2=="L") || (s1=="S" && s2=="M") || (s1=="S" && s2=="L") || (ch1=='S' && ch2=='M') || (ch1=='S' && ch2=='L') || (ch1=='M' && ch2=='L')){
        return "<";
    }
    else if((s1=="L" && s2=="M") || (s1=="M" && s2=="S") || (s1=="L" && s2=="S") || (ch1=='M' && ch2=='S') || (ch1=='L' && ch2=='S') || (ch1=='L' && ch2=='M')){
        return ">";
    }
    
    if(ch1=='L' && ch2=='L'){
        if(s1.length()>s2.length()){
            return ">";
        }
        else if(s1.length()<s2.length()){
            return "<";
        }
    }
    else if(ch1=='S' && ch2=='S'){
        if(s1.length()>s2.length()){
            return "<";
        }
        else if(s1.length()<s2.length()){
            return ">";
        }
    }
}
 
 
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int tc;
    cin>>tc;
    while(tc--){
        cout<<func()<<"\n";
    }
    return 0;
}
 