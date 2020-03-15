#include <iostream>
#include <vector>
#include <string>
using namespace std;


/*
3
yellow_hat headgear
sunglasses eyewear
green_turban headgear

3
crow_mask face
blue_sunglasses face
smoky_makeup face

6
yellow_hat head
green_hat head
blue_hat head
tshirts body
sshirts body
pants bottom
*/


int glo[30];
int ans = 0;
void Comb(int* set, int set_size, int m, int n, int index) {
	if (set_size == n) {
		int answer = 1;
		for (int i = 0; i < set_size; i++) {
			answer *= glo[set[i]];
		}
		ans += answer;
		return;
	} if (index == m) return;

	set[set_size] = index;

	Comb(set, set_size + 1, m, n, index + 1);
	Comb(set, set_size, m, n, index + 1);
}
int solution(vector<vector<string>> clothes) {
	vector<pair<string, int>> str;
	vector<string> clothing = clothes.back();
	int count_num = 0;
	int* set = new int[1000];
	for (int i = 0; i < 1000; i++) {
		set[i] = 0;
	}
	while (!clothing.empty()) {
		for (auto it = str.begin(); it != str.end(); ++it) {
			if ((*it).first == clothing.back()) {
				(*it).second++;
				count_num++;
			}
		}
		if (count_num == 0)
			str.push_back(make_pair(clothing.back(), 1));
		count_num = 0;
		clothing.pop_back();
		clothing.pop_back();
	}
	count_num = str.capacity();
	for (int i = 0; i < count_num; i++) {
		glo[i] = str.back().second;
		str.pop_back();
	}

	for (int i = 1; i <= count_num; i++) {
		Comb(set, 0, count_num, i, 0);
	}
	return ans;
}
int main() {
	int n;
	string cloth;
	vector<string> clothing;
	vector<vector<string>> clothes;
	
	cin >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < 2; j++) {
			cin >> cloth;
			clothing.push_back(cloth);
		}
		clothes.push_back(clothing);
	}
	
	int answer = solution(clothes);
	cout << answer << endl;
}