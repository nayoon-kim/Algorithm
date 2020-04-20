#include <iostream>
#include <queue>
//≈ª√‚
using namespace std;
int R, C;
int dir[4][2] = { {1, 0}, {-1, 0}, {0, 1}, {0, -1} };
int start_x, start_y;
queue<pair<int, int>> water;
queue<pair<int, int>> animal;

void bfs(int S[50][50]) {
	
	queue<pair<int, int>> _w = water;
	while (!_w.empty()) {
		pair<int, int> p = _w.front();
		_w.pop();
		for (int i = 0; i < 4; i++) {
			if (p.first + dir[i][0] > -1 && p.first + dir[i][0] < R && p.second + dir[i][1] > -1 && p.second + dir[i][1] < C) {
				if (S[p.first + dir[i][0]][p.second + dir[i][1]] == 0 || S[p.first + dir[i][0]][p.second + dir[i][1]] == 1) {
					S[p.first + dir[i][0]][p.second + dir[i][1]] = 2;
					water.push(make_pair(p.first + dir[i][0], p.second + dir[i][1]));
				}
			}
		}
	}
	queue<pair<int, int>> _animal = animal;

	while (!_animal.empty()) {
		pair<int, int> _a = _animal.front();
		_animal.pop();
		animal.pop();

		S[_a.first][_a.second] = 0;
			for (int i = 0; i < 4; i++) {
				if (_a.first + dir[i][0] > -1 && _a.first + dir[i][0] < R && _a.second + dir[i][1] > -1 && _a.second + dir[i][1] < C) {
					if (S[_a.first + dir[i][0]][_a.second + dir[i][1]] == 0) {
						S[_a.first + dir[i][0]][_a.second + dir[i][1]] = 1;
						animal.push(make_pair(_a.first + dir[i][0], _a.second + dir[i][1]));
					}
					else if (S[_a.first + dir[i][0]][_a.second + dir[i][1]] == 3) {
						start_x = _a.first + dir[i][0];
						start_y = _a.second + dir[i][1];
						return;
					}
				}
			}
	}
	
}

int main() {
	int S[50][50];
	int num[50][50];
	char input;
	int end_x, end_y;
	int min = 0;
	cin >> R >> C;
	start_x = -1, start_y = -1;
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {

			cin >> input;

			if (input == '.')
				S[i][j] = 0;
			else if (input == 'S') {
				S[i][j] = 1;
				animal.push(make_pair(i, j));
			}
			else if (input == '*') {
				S[i][j] = 2;
				water.push(make_pair(i, j));
			}
			else if (input == 'D') {
				S[i][j] = 3;
				end_x = i;
				end_y = j;
			}
			else
				S[i][j] = 4;

			num[i][j] = 0;
		}
	}
	while (true) {
		
		if (animal.empty()) {
			cout << "KAKTUS" << endl;
			break;
		}
		else {
			bfs(S);
			min++;
		}

		if (start_x == end_x && start_y == end_y) {
			cout << min << endl;
			break;
		}
	}
	
}

