/**
 *    author:  tourist
 *    created: 26.03.2021 16:39:26       
**/
#include <bits/stdc++.h>

using namespace std;

int Detect(vector<string> s) {
  int n = (int) s.size();
  int m = (int) s[0].size();
  assert(n == 100 && m == 10000);
  vector<int> take(m, 0);
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      if (s[i][j] == '1') { 
        take[j] += 1;
      }
    }
  }
  vector<int> order(m);
  iota(order.begin(), order.end(), 0);
  sort(order.begin(), order.end(), [&](int i, int j) {
    return take[i] > take[j];
  });
  vector<double> area(n, 0);
  for (int i = 0; i < n; i++) {
    int k0 = 0;
    int k1 = 0;
    int ps = 0;
    for (int j : order) {
      if (s[i][j] == '1') {
        ps += k0;
        k1 += 1;
      } else {
        k0 += 1;
      }
    }
    area[i] = 1.0 * ps / (k0 * k1);
  }
  return (int) (max_element(area.begin(), area.end()) - area.begin());
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  #ifdef LOCAL
    mt19937 rng(58);
    uniform_real_distribution<double> urd(0, 1);
    int res = 0;
    int tcount = 50;
    for (int tc = 0; tc < tcount; tc++) {
      int n = 100;
      int m = 10000;
      vector<string> a(n, string(m, '0'));
      vector<double> skill(n);
      vector<double> difficulty(m);
      for (int i = 0; i < n; i++) {
        skill[i] = urd(rng) * 6 - 3;
      }
      for (int i = 0; i < m; i++) {
        difficulty[i] = urd(rng) * 6 - 3;
      }
      int cheater = rng() % n;
      for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
          double prob = 1 / (1 + exp(difficulty[j] - skill[i]));
          a[i][j] = (urd(rng) < prob ? '1' : '0');
        }
        if (i == cheater) {
          for (int j = 0; j < m; j++) {
            if (rng() & 1) {
              a[i][j] = '1';
            }
          }
        }
      }
      int got = Detect(a);
      cerr << got << " " << cheater << " " << (got == cheater) << '\n';
      res += (got == cheater ? 1 : 0);
    }
    cerr << res << " " << tcount << '\n';
  #else
    int tt;
    cin >> tt;
    int p;
    cin >> p;
    for (int qq = 1; qq <= tt; qq++) {
      cout << "Case #" << qq << ": ";
      vector<string> a(100);
      for (int i = 0; i < 100; i++) {
        cin >> a[i];
      }
      int x = Detect(a);
      cout << x + 1 << '\n';
    }
  #endif
  return 0;
}
