#include<iostream>
using namespace std;

int main(){
    int t;
    cin>>t;
    for(int _=0;_<t;_++){
        int n,q;
        cin>>n,q;
        int array[n],sum=0;
        for(int i=0;i<n;i++){
            cin>>array[n];
            sum+=array[n];
        }
        int array2[q][2];
        for(int i=0;i<q;i++){
            cin>>array2[i][0];
            cin>>array2[i][1];
        }
        for(int i=0;i<q;i++){
            int rem=array2[i][1]-array2[i][0];
            rem++;
            if(rem%2!=0){
                sum++;
            }
        }
        cout<<sum<<endl;
    }
    return 0;
}