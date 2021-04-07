#include <bits/stdc++.h>
using namespace std;

void solve(int t){
	int n = 100;
	int q = 10000;
	vector<string> a(n);
	for(string& s : a) cin >> s;
	vector<int> psolved(n), qsolved(q);
	for(int i = 0; i < n; i++) for(int j = 0; j < q; j++){
		if(a[i][j] == '1'){
			psolved[i]++;
			qsolved[j]++;
		}
	}
	vector<int> pord(n);
	vector<int> qord(q);
	for(int i = 0; i < n; i++) pord[i] = i;
	for(int i = 0; i < q; i++) qord[i] = i;
	sort(pord.begin(), pord.end(), [&](int x, int y){
		return psolved[x] < psolved[y];
	});
	sort(qord.begin(), qord.end(), [&](int x, int y){
		return qsolved[x] > qsolved[y];
	});
	vector<double> score(n);
	for(int i = 0; i < n; i++){
		int n0 = 0;
		int n1 = 0;
		int inv = 0;
		for(int j = 0; j < q; j++){
			if(a[pord[i]][qord[j]] == '1'){
				n1++;
				inv += n0;
			} else {
				n0++;
			}
		}
		double f = inv;
		f /= n0;
		f /= n1;
		score[i] = f;
	}
	int best = 0;
	for(int i = 0; i < n; i++){
		if(score[i] > score[best]) best = i;
	}
	cout << "Case #" << t << ": ";
	cout << (pord[best] +1) << '\n';
}

int main(){
	ios_base::sync_with_stdio(false), cin.tie(nullptr);
	int T, P;
	cin >> T >> P;
	for(int t = 1; t <= T; t++) solve(t);
}