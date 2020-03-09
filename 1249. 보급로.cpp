#include <iostream>
#include <queue>
using namespace std;

int input;
int** arr, **_array;

void bfs() {

	queue<pair<int, int>> que;
	que.push(make_pair(0, 0));
	while (!que.empty()) {

		pair<int, int> p = que.front();
		int p1 = p.first;
		int p2 = p.second;
		que.pop();

		cout << "_array[" << p1 << "][" << p2 << "]: " << _array[p1][p2] << endl;
		if (p1 + 1 < input) {
			if (_array[p1 + 1][p2] == -1 || _array[p1 + 1][p2] > _array[p1][p2] + arr[p1 + 1][p2]) {
				_array[p1 + 1][p2] = _array[p1][p2] + arr[p1 + 1][p2];
				que.push(make_pair(p1 + 1, p2));
			}
		}
		if (p1 - 1 > -1) {
			if (_array[p1 - 1][p2] == -1 || _array[p1 - 1][p2] > _array[p1][p2] + arr[p1 - 1][p2]) {
				_array[p1 - 1][p2] = _array[p1][p2] + arr[p1 - 1][p2];
				que.push(make_pair(p1 - 1, p2));
			}
		}
		if (p2 + 1 < input) {
			if (_array[p1][p2 + 1] == -1 || _array[p1][p2 + 1] > _array[p1][p2] + arr[p1][p2 + 1]) {
				_array[p1][p2 + 1] = _array[p1][p2] + arr[p1][p2 + 1];
				que.push(make_pair(p1, p2 + 1));
			}
		}
		if (p2 - 1 > -1) {
			if (_array[p1][p2 - 1] == -1 || _array[p1][p2 - 1] > _array[p1][p2] + arr[p1][p2 - 1]) {
				_array[p1][p2 - 1] = _array[p1][p2] + arr[p1][p2 - 1];
				que.push(make_pair(p1, p2 - 1));
			}

		}
	}
}

int main() {
	int T;
	int test_case;
	scanf_s("%d", &T);

	for (test_case = 1; test_case <= T; test_case++) {

		scanf_s("%d", &input);
		arr = new int*[input];
		_array = new int*[input];

		for (int i = 0; i < input; i++) {
			arr[i] = new int[input];
			_array[i] = new int[input];
		}
		for (int i = 0; i < input; i++) {
			for (int j = 0; j < input; j++) {
				scanf_s("%1d", &arr[i][j]);
				_array[i][j] = -1;
			}
		}
		_array[0][0] = 0;
		bfs();

		printf("#%d %d\n", test_case, _array[input - 1][input - 1]);
	}
}