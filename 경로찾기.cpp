#include <iostream>
#include <queue>
using namespace std;
int n;
int arr[100][100];
bool visited[100];

void found(int start) {
	visited[start] = true;

	for (int i = 0; i < n; i++) {
		if (arr[start][i] == 1) {

			if (!visited[i]) {
				found(i);
			}
			for (int j = 0; j < n; j++) {
				if (arr[i][j] == 1)
					arr[start][j] = arr[i][j];
			}
		}

	}

}

int main() {

	cin >> n;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> arr[i][j];
			visited[i] = false;
		}
	}
	//cout << endl;
	//found(0);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			visited[j] = false;
		}
		found(i);
		//cout << i << endl;
		//for (int i = 0; i < n; i++) {
		//	for (int j = 0; j < n; j++) {
		//		cout << arr[i][j] << " ";
		//	}
		//	cout << endl;
		//}
		//cout << endl;
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cout << arr[i][j] << " ";
		}
		cout << endl;
	}
}