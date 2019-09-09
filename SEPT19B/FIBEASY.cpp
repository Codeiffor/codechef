#include <bits/stdc++.h>
using namespace std;

long long int square(int n) {
  long long int x = 1;
  while (n--) {
    x *= 2;
  }
  return x;
}

long long int floorPower2(long long int n) {
  int power = 0;
  for (int i = 0; i <= 60; i++) {
    if (n >= square(i)) {
      power = i;
    }
  }
  return square(power) - 1;
}

int main() {
  int x = 60;
  int a[x];
  a[0] = 0, a[1] = 1;
  for (int i = 2; i < x; i++) {
    a[i] = (a[i - 1] + a[i - 2]) % 10;
  }

  long long int t, n;
  cin >> t;
  while (t--) {
    cin >> n;
    long long int x = floorPower2(n);
    int index = x % 60;
    cout << a[index] << endl;
  }
  return 0;
}
