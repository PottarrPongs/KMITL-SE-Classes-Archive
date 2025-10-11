package Lab12ab;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Iterator;
import java.util.List;
import java.util.ListIterator;
import java.util.PriorityQueue;
import java.util.stream.IntStream;

import javax.rmi.ssl.SslRMIClientSocketFactory;

import Lab12ab.pack.*;

public class Lab12b_Graph2_671352 {
    static final int INF = Integer.MAX_VALUE;

    public static void main(String args[]) {
        q4();
        q5_call_dijkstra_adjacencyList();
    }

    static void q4() {
        int [][] q4_distanceBetween = { {   0,   4,    5,  INF,  INF,  INF},
                                        {   4,   0,   11,    9,    7,  INF},
                                        {   5,   11,   0,  INF,    3,  INF},
                                        { INF,    9, INF,    0,   13,    2},
                                        { INF,    7,   3,   13,    0,    6},
                                        { INF,  INF, INF,    2,    6,    0} };
        int A, B, C, D, E, F; A = 0; B = 1; C = 2; D = 3; E = 4; F = 5;
        System.out.println("djikstra from A");
        q4_dijkstra_pq(q4_distanceBetween, A);
            // exploring 0 [0, 4, 5, 2147483647, 2147483647, 2147483647]
            // exploring 1 [0, 4, 5, 13, 11, 2147483647]
            // exploring 2 [0, 4, 5, 13, 8, 2147483647]
            // exploring 4 [0, 4, 5, 13, 8, 14]
            // exploring 3 [0, 4, 5, 13, 8, 14]
            // exploring 5 [0, 4, 5, 13, 8, 14]
            // prev= [-1, 0, 0, 1, 2, 4]    
            // 0->2->4 
    }
    static void q4_dijkstra_pq(int[][] graph, int source) {
        int n = graph.length;
        int[] distance = new int[n];
        int[] prev = new int[n];
        boolean[] visited = new boolean[n];

        Arrays.fill(distance, INF);
        Arrays.fill(prev, -1);
        distance[source] = 0;

        // PriorityQueue stores (distance, node)
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        pq.offer(new int[]{0, source});

        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int dist = curr[0];
            int u = curr[1];

            if (visited[u]) continue; // skip if already processed
            visited[u] = true;

            // relax neighbors
            for (int v = 0; v < n; v++) {
                if (graph[u][v] != 0 && graph[u][v] != INF) {
                    int newDist = dist + graph[u][v];
                    if (newDist < distance[v]) {
                        distance[v] = newDist;
                        prev[v] = u;
                        pq.offer(new int[]{distance[v], v});
                    }
                }
            }
            System.out.println("exploring " + u + " " + Arrays.toString(distance));
        }
        System.out.println("prev= " + Arrays.toString(prev));
        q4_extractPath(prev, 4);
    }    
    static void q4_extractPath(int[] prev, int city) {
        ArrayList<Integer> reverse = new ArrayList<>(city);
        int at = city;
        while (at != -1) {
            reverse.add(at);
            at = prev[at];
        }
        StringBuilder sb = new StringBuilder();
        ListIterator<Integer> iter =  reverse.listIterator(reverse.size());
        while (iter.hasPrevious()) {
            sb.append(iter.previous()).append("->");
        }
        sb.delete(sb.length() - 2, sb.length());
        System.out.println(sb.toString());
    }

static void q5_call_dijkstra_adjacencyList() {
    // int [][] adjacencyMatrix = { {   0,   4,    5,  INF,  INF,  INF},
    //                              {   4,   0,   11,    9,    7,  INF},
    //                              {   5,   11,   0,  INF,    3,  INF},
    //                              { INF,    9, INF,    0,   13,    2},
    //                              { INF,    7,   3,   13,    0,    6},
    //                              { INF,  INF, INF,    2,    6,    0} };
    List<int[]> edges = Arrays.asList(new int[][]{
                                                {0,1,4}, {0,2,5}, 
                                                {1,2,11}, {1,3,9}, {1,4,7}, 
                                                {2,4,3}, 
                                                {3,4,13}, {3,5,2}, 
                                                {4,5,6}}); 
    int A, B, C, D, E, F; A = 0; B = 1; C = 2; D = 3; E = 4; F = 5;
    int numVertices = 6; // else loop through both edge[0] and edge[1] from edges to find maxId -> numVertices = maxId + 1;
    List<List<int[]>> graph = new ArrayList<>();
    for (int i = 0; i < numVertices; i++)
        graph.add(new ArrayList<>());     // List of <List of weighted edges>

    for (int[] edge: edges) {
        int i = edge[0];
        int j = edge[1];
        int weight = edge[2];
        graph.get(i).add(new int[]{weight, j});
        graph.get(j).add(new int[]{weight, i});
    }

    int startNode = C;  // 2
    q5b_dijstra_adjaList(graph, startNode);
        // ???
        // ???
        // prev= ???
        // Furthest city is 3, distance= 11
}
    static void q5b_dijstra_adjaList(List<List<int[]>> graph, int startNode) {
        int numVertices = graph.size();
        int[] dist = new int[numVertices];
        int[] prev = new int[numVertices];
        
        Arrays.fill(dist, INF);
        Arrays.fill(prev, -1);
        dist[startNode] = 0;

        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        pq.add(new int[]{ 0, startNode });

        while (!pq.isEmpty()) {
            int[] pair = pq.poll();
            int cur_distance = pair[0];
            int u = pair[1];

            if (cur_distance > dist[u])
                continue;   // distance to u is alreay closer to startNode
            System.out.println("exploring " + u + " " + Arrays.toString(dist));

            for (int[] edge :  graph.get(u)) {
                int weight = edge[0];
                int v = edge[1];

                if (dist[u] != INF && dist[u] + weight < dist[v]) {
                    // going to v via u is closer
                    dist[v] = dist[u] + weight;
                    prev[v] = u;
                    pq.add(new int[]{dist[v],v});
                }
            }
        }
        System.out.println("prev= " + Arrays.toString(prev));
        int[] ans = q5c_furthest_distance(dist);
        System.out.println("Furthest city is " + ans[0] + ", distance= " + ans[1]);
    }
    static int[] q5c_furthest_distance(int[] dist) {
        int maxDist = -1;
        int furthestCity = -1;

        for (int i = 0; i < dist.length; i++) {
            // Check for reachable nodes (distance is not infinity)
            if (dist[i] != INF) {
                if (dist[i] > maxDist) {
                    maxDist = dist[i];
                    furthestCity = i;
                }
            }
        }
        return new int[]{ furthestCity, maxDist };
    }
}
