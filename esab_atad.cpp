#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    string s;
    cin>>s;
    while(t--)
    {
        char c,o;
        string a="";
        for(int i=0;i<10;i++)
        {
            a+="0";
        }
        for(int i=1;i<=10;i++)
        {
            cout<<i<<endl;
            fflush(stdout);
            cin>>c;
            a[i-1]=c;
        }
        cout<<a<<endl;
        fflush(stdout);
        cin>>o;
        if(o=='N')
            return 0;
        else
            continue;
    }
    return 0;
}