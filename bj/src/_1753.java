import java.io.*;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class _1753 {
    static class Node{
        int no;
        int distance;
        Node link;

        public Node(int no, int distance, Node link) {
            super();
            this.no = no;
            this.distance = distance;
            this.link = link;
        }

        @Override
        public String toString() {
            return "no: " + no +", distance: " + distance + "link: " + link;
        }
    }
    static class Vertex implements Comparable<Vertex>{
        int no;
        int distance;

        public Vertex(int no, int distance) {
            super();
            this.no = no;
            this.distance = distance;
        }

        @Override
        public int compareTo(Vertex o) {
            return this.distance - o.distance;
        }

        @Override
        public String toString() {
            return "no: " + no +", distance: " + distance;
        }
    }
    public static void main(String[] args) throws Exception{
        System.setIn(new FileInputStream("res/input1753.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int V = Integer.parseInt(st.nextToken()), E = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(br.readLine());
        Node[] nodes = new Node[V + 1];
        boolean[] visited = new boolean[V + 1];
        int[] distance = new int[V + 1];
        Arrays.fill(distance, Integer.MAX_VALUE);

        for(int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int u = Integer.parseInt(st.nextToken()), v = Integer.parseInt(st.nextToken()), w = Integer.parseInt(st.nextToken());
            nodes[u] = new Node(v, w, nodes[u]);
        }

        PriorityQueue<Vertex> pq = new PriorityQueue<>();
        pq.offer(new Vertex(K, 0));
        distance[K] = 0;

        Vertex current;
        Node node;
        while(!pq.isEmpty()) {
            current = pq.poll();
            if (visited[current.no] || distance[current.no] < current.distance) continue;

            visited[current.no] = true;
            for(node = nodes[current.no]; node != null; node=node.link) {
                if (!visited[node.no] && current.distance + node.distance < distance[node.no]) {
                    distance[node.no] = current.distance + node.distance;
                    pq.offer(new Vertex(node.no, distance[node.no]));
                }
            }
        }
        StringBuilder sb = new StringBuilder();
        for(int i = 1; i < V + 1; i++) {
            if (distance[i] == Integer.MAX_VALUE)
                sb.append("INF").append("\n");
            else
                sb.append(distance[i]).append("\n");
        }
        System.out.println(sb.toString());
    }
}
