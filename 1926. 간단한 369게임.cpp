#include <iostream>
using namespace std;

int* func(int arr[], int num) {
	int n = 0, count_num = 0;
	int number = 1000;
	while (true) {
		if (num / 10 == 0) {
			arr[n] = num;
			n++;
			break;
		}
		arr[n] = num / number;
		num %= number;
		n++;
		number /= 10;
	}
	for (int i = 0; i < n; i++) {
		if (arr[i] != 0 && arr[i] % 3 == 0)
			count_num++;
	}
	arr[4] = count_num;

	return arr;
}

int main() {
	int n;
	cin >> n;
	int i = 1, count_num = 0;
	int* arr = new int[5];
	for (int i = 0; i < 5; i++) {
		arr[i] = -1;
	}
	while (i <= n) {
		func(arr, i);
		if (arr[4] != 0) {
			for (int k = 0; k < arr[4]; k++)
				cout << "-";
		}
		else
			cout << i;
		i++;
		count_num = 0;
		cout << " ";
	}
}