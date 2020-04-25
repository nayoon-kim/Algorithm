#include <iostream>
#include <queue>
using namespace std;
int M, N, H;
int T[100][100][100];
int D[6][3] = { {1, 0, 0}, {-1, 0, 0}, {0, 1, 0}, {0, -1, 0}, {0, 0, 1}, {0, 0, -1} };
int ing_tomato = 0;

queue<pair<pair<int, int>, int>> tomato(queue<pair<pair<int,int>,int>> tom) {
	queue<pair<pair<int, int>, int>> result;
	pair<pair<int, int>, int> p;
	while (!tom.empty()) {
		p = tom.front();
		tom.pop();
		for (int i = 0; i < 6; i++) {

			if (p.first.first + D[i][0] > -1 && p.first.first + D[i][0] < H
				&& p.first.second + D[i][1] > -1 && p.first.second + D[i][1] < N
				&& p.second + D[i][2] > -1 && p.second + D[i][2] < M) {
				if (T[p.first.first + D[i][0]][p.first.second + D[i][1]][p.second + D[i][2]] == 0) {
					T[p.first.first + D[i][0]][p.first.second + D[i][1]][p.second + D[i][2]] = 1;
					result.push(make_pair(make_pair(p.first.first + D[i][0], p.first.second + D[i][1]), p.second + D[i][2]));
					ing_tomato++;
				}
			}

		}
	}
	return result;
}

int main() {
	int input;
	int total_tomato = 0;
	int min = 0;
	queue<pair<pair<int, int>, int>> q;
	cin >> M >> N >> H;
	total_tomato = M * N * H;

	for (int i = 0; i < H; i++) {
		for (int j = 0; j < N; j++) {
			for (int k = 0; k < M; k++) {
				cin >> input;
				T[i][j][k] = input;
				if (input == 1) {
					q.push(make_pair(make_pair(i, j), k));
					ing_tomato++;
				}
				else if (input == -1)
					total_tomato -= 1;
			}
		}
	}


	while (true) {
		if (ing_tomato == total_tomato) {
			cout << min << endl;
			break;
		}
		if (q.empty()){
			cout << -1 << endl;
			break;
		}
		else {
			q = tomato(q);
			min++;
		}
	}
}