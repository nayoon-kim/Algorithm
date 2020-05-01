#include <iostream>
#include <queue>
using namespace std;
int M, N;
int tomato[1000][1000];
int dir[4][2] = { {1, 0}, {-1, 0}, {0, 1}, {0, -1} };

queue<pair<int, int>> bfs(queue<pair<int, int>> q) {
	queue<pair<int, int>> s;

	while (!q.empty()) {
		pair<int, int> p = q.front();
		q.pop();

		for (int i = 0; i < 4; i++) {
			if (p.first + dir[i][0] > -1 && p.first + dir[i][0] < N && p.second + dir[i][1] > -1 && p.second + dir[i][1] < M) {
				if (tomato[p.first + dir[i][0]][p.second + dir[i][1]] == 0) {
					tomato[p.first + dir[i][0]][p.second + dir[i][1]] = 1;
					s.push(make_pair(p.first + dir[i][0], p.second + dir[i][1]));
				}
					
			}
		}

	}

	return s;
}

int main() {
	cin >> M >> N;
	int to_max = M * N;
	int to_cur = 0;
	int min_date = 0;
	queue<pair<int, int>> q;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> tomato[i][j];
			if (tomato[i][j] == -1)
				to_max -= 1;
			else if (tomato[i][j] == 1) {
				q.push(make_pair(i, j));
				to_cur++;
			}
		}
	}

	while (to_cur != to_max) {
		if (q.size() == 0) {
			min_date = -1;
			break;
		}
		else {
			q = bfs(q);
			min_date += 1;
			to_cur += q.size();
			//cout << to_cur << endl;
			//for (int i = 0; i < N; i++) {
			//	for (int j = 0; j < M; j++) {
			//		cout << tomato[i][j] << " ";
			//	}
			//	cout << endl;
			//}
			//cout << endl;
		}
	}
	cout << min_date << endl;
}