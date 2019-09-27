#include <bits/stdc++.h>
using namespace std;

double fact(double x) {
  if (x <= 1)
    return 1;
  return x * fact(x - 1);
}

double nCr(int n, int r) { return fact(n) / fact(n - r) / fact(r); }

int main() {
  int t, n, k;
  cin >> t;
  while (t--) {
    cin >> n >> k;
    int arr[n];
    for (int i = 0; i < n; i++)
      cin >> arr[i];
    sort(arr, arr + n);
    int x = count(arr, arr + n, arr[k-1]);
    int y = count(arr, arr + k, arr[k-1]);
    cout.precision(0);
    cout << fixed << nCr(x, y) << endl;
  }

  return 0;
}