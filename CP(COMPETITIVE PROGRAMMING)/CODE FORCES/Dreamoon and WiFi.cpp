#include<bits/stdc++.h> 
using namespace std;
 
#define sl(x)	        cin>>x
#define sl2(x,y)        cin>>x>>y
#define pl(x)           cout<<x<<"\n"
#define pl2(x,y) 		cout<<x<<" "<<y<<"\n"
#define pl3(x)			cout<<x<<" "
#define all(x)          x.begin(), x.end()
#define  tup(su)        transform(su.begin(), su.end(), su.begin(), ::toupper);
#define  tlo(sl)        transform(sl.begin(), sl.end(), sl.begin(), ::tolower);
#define F               first
#define S               second
#define ll              long long int
#define deb(x)          cout << #x << "=" << x << endl   //Debugging
#define deb2(x, y)      cout << #x << "=" << x << "," << #y << "=" << y << endl  //Debugging
#define pb              push_back
#define mp              make_pair
#define vp              vector<pair <ll,ll> >
#define pii             pair<int,int>
#define vi              vector<int>
#define mii             map<int,int>
#define mci             map<char,int>
#define pqb             priority_queue<int>
#define pqs             priority_queue<int,vi,greater<int> >
#define setbits(x)      __builtin_popcountll(x)
#define zrobits(x)      __builtin_ctzll(x)
#define mod             1000000007
#define inf             1e18
#define sp(x,y)         cout << setprecision(y) << x << '\n';
#define mk(arr,n,type)  type *arr=new type[n];
#define PI 				3.1415926535897932384626
#define clr(x) 	 	 	memset(x, 0, sizeof(x))
#define fo(i,x,n)    	for(ll i=x;i<n;i++)   //for loop
#define fj(i,x,n)	 	for(i=x;i<n;i++)
#define fx(i,x,n)    	for(ll i=x;i>=n;i--)  //decreasing loop


ll fact(ll n);
bool sortbysec(const pair<int,int> &a, const pair<int,int> &b) 
{ 
    return (a.second < b.second); 
}
  
ll nCr(ll n, ll r) 
{ 
    return fact(n) / (fact(r) * fact(n - r)); 
} 
  
// Returns factorial of n 
ll fact(ll n) 
{ 
    ll res = 1; 
    for (ll i = 2; i <= n; i++) 
        res = res * i; 
    return res; 
} 

int main() 
{
    ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    srand(chrono::high_resolution_clock::now().time_since_epoch().count());
    ll t=1;
    // sl(t);
    while(t--)
    {  	
		string s1,s2;
		ll po=0,p=0,mo=0,m=0,q=0,dp,dm,l;
		double pr,ans,tp;
		sl2(s1,s2);
		l = s1.length();
		fo(i,0,l)
		{
			if(s1[i]=='+')
				po++;
			else
				mo++;
			if(s2[i]=='+')
				p++;
			else if(s2[i]=='-')
				m++;
			else
				q++;
		}
		if(p>po||m>mo)
			pr = 0;
		else
		{
			dp = po-p;
			dm = mo-m;
			tp = pow(2,q);
			ans = nCr(q,dm);
			pr = (double)(ans/tp);
		}
		sp(pr,10);
	}
}