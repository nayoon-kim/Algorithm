#include<iostream>

using namespace std;
int n, b, s, top_len, min_num;
int* h;
void comb(int* set, int set_size, int m, int n, int index) {
	if (set_size == n) {
		top_len = s;
		for (int i = 0; i < set_size; i++) {
			top_len -= h[set[i]];
		}
		if (min_num > (top_len - b) && top_len >= b) {
			min_num = top_len - b;
			cout << min_num << endl;
		}
		return;
	}
	if (m == index) return;

	set[set_size] = index;

	comb(set, set_size + 1, m, n, index + 1);
	comb(set, set_size, m, n, index + 1);
}
int main(int argc, char** argv)
{
	int test_case;
	int T;
	int *temp;
	cin >> T;

	for (test_case = 1; test_case <= T; ++test_case)
	{
		cin >> n >> b;
		s = 0, top_len = 0;
		h = new int[n];
		temp = new int[n];
		for (int i = 0; i < n; i++) {
			cin >> h[i];
			s += h[i];
		}
		top_len = s;
		min_num = s;
		for (int i = 0; i <= n; i++) {
			comb(temp, 0, n, i, 0);
		}

		cout << "#" << test_case << " " << min_num << endl;

	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}