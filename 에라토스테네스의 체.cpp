#include <iostream>
using namespace std;

int number, re_number;
int a[1001];
int re[1001];

void primeNumber() {
	int n = 1;
	for (int i = 2; i <= number; i++) {
		a[i] = i;
	}
	for (int i = 2; i <= number; i++) {
		if (a[i] == 0) continue;
		for (int j = i; j <= number; j += i) {
			if (a[j] == 0) continue;
			a[j] = 0;
			re[n] = j;
			n++;
		}
	}
	cout << re[re_number] << endl;
}

int main() {
	cin >> number >> re_number;
	primeNumber();
}