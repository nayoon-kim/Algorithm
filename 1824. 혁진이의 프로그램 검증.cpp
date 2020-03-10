#include <iostream>
#include <string>
#include <random>
#include <time.h>
using namespace std;

int r, c;

enum DIR { up, down, right, left };

string func(string* _array, int a, int b, DIR dir, int mem) {
	int ran = 0;
	int count_num = 1000;
	string arr[4];
	while (count_num > 0) {
		//cout << "_array["<<a<<"]["<<b<<"]: " <<_array[a].at(b)<<" mem: "<<mem << endl;
		switch (_array[a].at(b)) {
		case '<':
			dir = DIR::left;
			break;
		case '>':
			dir = DIR::right;
			break;
		case '^':
			dir = DIR::up;
			break;
		case 'v':
			dir = DIR::down;
			break;
		case '_':
			if (mem == 0) dir = DIR::right;
			else dir = DIR::left;
			break;
		case '|':
			if (mem == 0) dir = DIR::down;
			else dir = DIR::up;
			break;
		case '?':
			ran = 0;
			_array[a].at(b) = '>';
			arr[0] = func(_array, a, b, dir, mem);
			_array[a].at(b) = '^';
			arr[1] = func(_array, a, b, dir, mem);
			_array[a].at(b) = '<';
			arr[2] = func(_array, a, b, dir, mem);
			_array[a].at(b) = 'v';
			arr[3] = func(_array, a, b, dir, mem);
			//_array[a].at(b) = '?';
			for (string k : arr) {
				if (k == "YES") return "YES";
			}
			break;
		case '.':
			break;
		case '@':
			return "YES";
			break;
		case '+':
			if (mem == 15) mem = 0;
			else mem++;
			break;
		case '-':
			if (mem == 0) mem = 15;
			else mem--;
			break;
		default:
			mem = (int)(_array[a].at(b)) - 48;
		}

		if (dir == DIR::right) {
			if (b == c - 1) b = 0;
			else b++;
		}
		else if(dir == DIR::left){
			if (b == 0) b = c - 1;
			else b--;
		}
		else if (dir == DIR::up) {
			if (a == 0) a = r - 1;
			else a--;
		}
		else {
			if (a == r - 1) a = 0;
			else a++;
		}
		count_num--;
	}
	return "NO";
}

int main() {
	string* _array;
	cin >> r >> c;
	_array = new string[r];

	for (int i = 0; i < r; i++) {
		cin >> _array[i];
	}

	string a = func(_array, 0, 0, DIR::right, 0);
	//cout << a << endl;
	//for (int i = 0; i < r; i++) {
	//	for(int j = 0; j<c;j++)
	//		cout << _array[i].at(j) << endl;
	//}

}