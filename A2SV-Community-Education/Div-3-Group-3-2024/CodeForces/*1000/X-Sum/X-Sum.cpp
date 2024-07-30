#include <bits/stdc++.h>
using namespace std;

using ll = signed long long int;

void solve() {
    ll n, m;
    cin >> n >> m;
    vector<vector<ll>> grid(n, vector<ll>(m));

    for (ll i = 0; i < n; i++)
        for (ll j = 0; j < m; j++)
            cin >> grid[i][j];

    ll max_sum = 0;
    for (ll i = 0; i < n; i++) {
        for (ll j = 0; j < m; j++) {
            ll temp_sum = grid[i][j]; // add the current square value 

            ll tempi = i - 1, tempj = j - 1; // go up and left until i and j are 0
            while (tempi >= 0 && tempj >= 0) {
                temp_sum += grid[tempi][tempj];
                tempi--, tempj--;
            }

            tempi = i + 1; tempj = j + 1; // go down and right until i and j are equal to n and m respectively
            while (tempi < n && tempj < m) {
                temp_sum += grid[tempi][tempj];
                tempi++, tempj++;
            }

            tempi = i - 1; tempj = j + 1; // go up and right until i is 0 and j is m - 1
            while (tempi >= 0 && tempj < m) {
                temp_sum += grid[tempi][tempj];
                tempi--, tempj++;
            }

            tempi = i + 1; tempj = j - 1; // go down and left until i is n - 1 and j is 0
            while (tempi < n && tempj >= 0) {
                temp_sum += grid[tempi][tempj];
                tempi++, tempj--;
            }

            max_sum = max(max_sum, temp_sum);
        }
    }
    cout << max_sum << "\n"; 
}

int main() {
    int t;
    cin >> t;
    while (t--)
        solve();

    return 0;
}