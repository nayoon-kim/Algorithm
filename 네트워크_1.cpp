#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int getParent(int* set, int k) {
	if (set[k] == k) return k;
	return set[k] = getParent(set, set[k]);
}
void unionParent(int* set, int a, int b) {
	a = getParent(set, a);
	b = getParent(set, b);

	if (a < b) set[b] = a;
	else set[a] = b;
}
int findParent(int* set, int a, int b) {
	a = getParent(set, a);
	b = getParent(set, b);
	if (a == b) return 1;
	else return 0;
}

int solution(int n, vector<vector<int>> computers) {
	int answer = 0;

	int counting_num = 1, num = 0;

	//set array¿¡ ¹èÄ¡
	int* set = new int[n + 1];
	for (int i = 1; i <= n; i++)
		set[i] = i;

	for (int i = 0; i < computers.size(); i++) {
		for (int j = 0; j < n; j++) {
			if (computers[i][j] == 1) {
				if (!findParent(set, counting_num, j + 1)) {
					num++;
					unionParent(set, counting_num, j + 1);
				}
			}
		}
		counting_num++;
	}

	cout << n << " " << num << endl;

	return answer;
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