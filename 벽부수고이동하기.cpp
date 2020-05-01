#ifdef _MSC_VER
#define _CRT_SECURE_NO_WARNINGS
#endif
#include <iostream>
#include <queue>
using namespace std;

struct Point {
	Point() {};
	Point(int x, int y, int distance, int wall, int value, bool visited) :X(x), Y(y), DISTANCE(distance), WALL(wall), VALUE(value), VISITED(visited) {}
	int X;
	int Y;
	int DISTANCE;
	int WALL;
	int VALUE;
	bool VISITED;
};

int N, M;
Point area[1000][1000];
int dir[4][2] = { {1, 0},{-1,0},{0, 1},{0, -1} };

int bfs(Point point) {
	queue<Point> q;
	q.push(point);

	while (!q.empty()) {
		Point p = q.front();
		q.pop();

		printf("%d %d %d %d %d \n", p.X,
			p.Y,
			p.WALL,
			p.DISTANCE, p.VALUE);

		if (p.X == M - 1 && p.Y == N - 1)
			break;
		for (int i = 0; i < 4; i++) {
			if (p.X + dir[i][0] > -1 && p.X + dir[i][0] < M && p.Y + dir[i][1] > -1 && p.Y + dir[i][1] < N && p.WALL < 2) {
				if (area[p.X + dir[i][0]][p.Y + dir[i][1]].VALUE == 1)
					area[p.X + dir[i][0]][p.Y + dir[i][1]].WALL += 1;
				area[p.X + dir[i][0]][p.Y + dir[i][1]].DISTANCE += 1;
				q.push(area[p.X + dir[i][0]][p.Y + dir[i][1]]);
				
			}
		}
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			printf("%d %d %d %d %d \n", area[i][j].X,
				area[i][j].Y,
				area[i][j].WALL,
				area[i][j].DISTANCE, area[i][j].VALUE);

		}
	}
	printf("\n");

	if (area[N - 1][M - 1].DISTANCE == 0)
		return -1;
	return area[N - 1][M - 1].DISTANCE;
}

int main() {
	scanf("%d %d", &N, &M);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			scanf("%1d", &area[i][j].VALUE);
			area[i][j].X = j;
			area[i][j].Y = i;
			area[i][j].WALL = 0;
			area[i][j].DISTANCE = 0;
			area[i][j].VISITED = false;
		}
	}
	bfs(area[0][0]);
	
}