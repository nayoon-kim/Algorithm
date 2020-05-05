#include <iostream>
#include <queue>
using namespace std;

int M, N;
int area[1000][1000];
int dir[4][2] = { {1, 0}, {-1, 0}, {0, 1}, {0, -1} };
bool escape = false;
queue<pair<int, int>> bfs1(queue<pair<int, int>> fire) {
	queue<pair<int, int>> _fire;

	while (!fire.empty()) {
		pair<int, int> f = fire.front();
		fire.pop();

		for (int i = 0; i < 4; i++) {
			if (f.first + dir[i][0] < N && f.first + dir[i][0] > -1 && f.second + dir[i][1] < M && f.second + dir[i][1] > -1) {
				if (area[f.first + dir[i][0]][f.second + dir[i][1]] == 0 || area[f.first + dir[i][0]][f.second + dir[i][1]] == 2) {
					area[f.first + dir[i][0]][f.second + dir[i][1]] = 1;
					_fire.push(make_pair(f.first + dir[i][0], f.second + dir[i][1]));
				}
			}
		}
	}
	return _fire;
}
queue<pair<int, int>> bfs2(queue<pair<int, int>> man) {
	queue<pair<int, int>> _man;

	while (!man.empty()) {
		pair<int, int> m = man.front();
		man.pop();
		
		for (int i = 0; i < 4; i++) {
			if (m.first + dir[i][0] < N && m.first + dir[i][0] > -1 && m.second + dir[i][1] < M && m.second + dir[i][1] > -1) {
				if (area[m.first + dir[i][0]][m.second + dir[i][1]] == 0) {
					if (area[m.first][m.second] == 0)
						area[m.first][m.second] = 2;
					area[m.first + dir[i][0]][m.second + dir[i][1]] = 2;
					_man.push(make_pair(m.first + dir[i][0], m.second + dir[i][1]));
					
				}
			}
			if (m.first + dir[i][0] == N || m.first + dir[i][0] == -1 || m.second + dir[i][1] == M || m.second + dir[i][1] == -1) {
				escape = true;
			}
			
		}
	}
	return _man;
}
int main() {
	int testcase;
	int result[100] = { 0, };
	char input;
	int min = 0;
	cin >> testcase;
	for (int k = 0; k < testcase; k++) {
		cin >> M >> N;
		queue<pair<int, int>> fire;
		queue<pair<int, int>> man;
		min = 0;
		escape = false;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				cin >> input;
				if (input == '.')
					area[i][j] = 0;
				else if (input == '#')
					area[i][j] = -1;
				else if (input == '@') {
					area[i][j] = 2;
					man.push(make_pair(i, j));
				}
				else {
					area[i][j] = 1;
					fire.push(make_pair(i, j));
				}
			}
		}
		while (true) {
			if (escape) {
				result[k] = min;
				break;
			}
			if (man.empty()) {
				result[k] = -1;
				break;
			}
			else {
				fire = bfs1(fire);
				man = bfs2(man);
			}
			min++;
		}

	}
	for (int k = 0; k < testcase; k++)
	{
		if (result[k] == -1)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << result[k] << endl;
	}
}