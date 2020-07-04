#include <iostream>
#include <set>
using namespace std;

int main() {
	int input;
	set<int> s;
	for (int i = 0; i < 10; i++) {
		cin >> input;
		s.insert(input % 42);
	}
	cout << s.size() << endl;
}