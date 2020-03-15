#include <iostream>
#include <vector>
using namespace std;

int targets, ans = 0;

void func(int* set, int set_size, int m) {

	if (set_size == m) {
		int result = 0;
		
		for (int i = 0; i < set_size; i++) {
			result += set[i];
		}
		if (result == targets) {
			ans++;
		}
		return;
	}

	func(set, set_size + 1, m);
	set[set_size] *= -1;
	func(set, set_size + 1, m);
}

int solution(vector<int> numbers, int target) {
	int answer = 0;
	int numbers_size = numbers.size();
	targets = target;
	int* set = new int[numbers_size];

	for (int i = 0; i < numbers_size; i++) {
		set[i] = numbers.back();
		numbers.pop_back();
	}
	func(set, 0, numbers_size);
	answer = ans;
	return answer;
}

int main() {

	int n, target,number;
	cin >> n >> target;

	vector<int> numbers;
	for (int i = 0; i < n; i++) {
		cin >> number;
		numbers.push_back(number);
	}
	
	cout << solution(numbers, target) << endl;

}