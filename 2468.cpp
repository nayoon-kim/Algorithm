#include <iostream>
#include <queue>
using namespace std;
int N;
int area[100][100];
int dir[4][2] = { {1, 0}, {-1, 0}, {0, 1}, {0, -1} };

int bfs(int number) {
	queue<pair<int, int>> q;
	bool visited[100][100] = { false, };

	int temp = 0;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (area[i][j] > number && !visited[i][j]) {
				//cout << "enter area[" << i << "][" << j << "]: " << area[i][j]<<endl;
				visited[i][j] = true;
				q.push(make_pair(i, j));
				temp++;
				while (!q.empty()) {
					
					pair<int, int> p = q.front();
					q.pop();
					for (int k = 0; k < 4; k++) {
						if (p.first + dir[k][0] > -1 && p.first + dir[k][0] < N && p.second + dir[k][1] > -1 && p.second + dir[k][1] < N) {
							if (area[p.first + dir[k][0]][p.second + dir[k][1]] > number && !visited[p.first + dir[k][0]][p.second + dir[k][1]]) {
								//cout<<"area[" << p.first + dir[k][0] << "][" << p.second + dir[k][1] << "]: " << area[p.first + dir[k][0]][p.second + dir[k][1]] << endl;
								visited[p.first + dir[k][0]][p.second + dir[k][1]] = true;
								
								q.push(make_pair(p.first + dir[k][0], p.second + dir[k][1]));
								
							}

						}
					}

				}
				
			}
		}
		
	}

	return temp;
}

int main() {
	int max_num = 0;
	int temp, number = 0;
	cin >> N;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> area[i][j];
			max_num = max_num < area[i][j] ? area[i][j] : max_num;
		}
	}
	
	for (int i = 0; i < max_num; i++) {
		
		temp = bfs(i);
		number = number > temp ? number : temp;
		//cout << temp << " " << number << endl;
	}
	cout << number << endl;


}