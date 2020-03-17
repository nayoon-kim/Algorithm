#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;


void dfs(int from, int n, vector<int> &visited, vector<vector<int>> &computers) {
	for (int i = 0; i < n; i++) {
		if (from != i && computers[from][i] == 1 && visited[i] == 0) {
			visited[i] = 1;
			dfs(i, n, visited, computers);
		}
	}
}
int solution(int n, vector<vector<int>> computers) {
	int network = 0;
	vector<int> visited(n, 0);

	for (int i = 0; i < n; i++) {
		if (visited[i] == 1)
			continue;

		network++;
		visited[i] = 1;
		dfs(i, n, visited, computers);
	}
	return network;
}

int main() {
	int n, com, answer;
	vector<int> computer;
	vector<vector<int>> computers;
	cin >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> com;
			computer.push_back(com);
		}
		computers.push_back(computer);
		computer.clear();
	}

	answer = solution(n, computers);
	cout << answer << endl;
}

/*5
1 1 0 0 1
1 1 0 0 1
0 0 1 0 0
0 0 1 0 0
1 1 0 0 1
1 1 0 0 1

3
1 1 0
1 1 0
0 0 1

5
1 1 0 0 1
1 1 0 0 1
0 0 1 0 0
0 0 1 0 0
1 1 0 0 1
1 1 0 0 1

*/