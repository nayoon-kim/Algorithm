#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int func(int* set, int k) {
	if (set[k] == k) return k;
	return set[k] = func(set, set[k]);
}

int solution(int n, vector<vector<int>> computers) {
	int answer = 0;
	int counting_num = 0;
	int* set = new int[n];
	int* s_set = new int[n];
	for (int i = 0; i < n; i++) {
		set[i] = i;
		s_set[i] = -1;
	}
	vector<int> computer;
	for (auto it = computers.begin(); it != computers.end(); ++it){
		computer = *it;

		for (int j = counting_num + 1; j < n; j++) {
			if (computer[j] == 1) {
				set[j] = counting_num;
				//cout << "computer set[" << j << "]: " << counting_num << endl;
			}
		}
		computer.clear();
		counting_num++;
	}

	for (int i = 0; i < n; i++) {
		func(set, i);
	}
	
	for (int i = 0; i < n; i++) {
		computer.push_back(set[i]);
	}
	sort(computer.begin(), computer.end());
	computer.erase(unique(computer.begin(), computer.end()), computer.end());
	answer = computer.size();
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