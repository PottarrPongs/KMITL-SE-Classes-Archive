package Lab12ab;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.stream.IntStream;
import java.util.Stack;

import Lab12ab.pack.*;

public class Lab12a_Graph1_671352 {
    final static int INF = Integer.MAX_VALUE;   // for q2
  
    public static void main(String args[]) {
        q1_1();
        q1_2();
        q1_3();
        q2();
        q3_1();
        q3_2();
        q3_3();
        q3_4();
    }

    static void q1_1() {
        System.out.println("Graph List");
        GraphList_671352 graphL = new GraphList_671352(5);
        graphL.addEdge(0, 1);
        graphL.addEdge(0, 4);
        graphL.addEdge(1, 2);
        graphL.addEdge(1, 3);
        graphL.printGraph();
            // 0 -> 1 4 
            // 1 -> 0 2 3
            // 2 -> 1
            // 3 -> 1
            // 4 -> 0        
        System.out.println(graphL.hasEdge(1, 3));   // true
        System.out.println(graphL.hasPath(4, 2) );  // true
        System.out.println(graphL.neighborsOf(2) );     // [1]

        System.out.println("DFS:");
        graphL.dfs(0); // 0 1 2 3 4
    }
    static void q1_2() {
        System.out.println("Graph Map");
        GraphMap_671352 graphM = new GraphMap_671352();
        graphM.addEdge(1, 2);
        graphM.addEdge(1, 3);
        graphM.addEdge(2, 4);
        graphM.printGraph();
            // 1 -> [2, 3]
            // 2 -> [1, 4]
            // 3 -> [1]
            // 4 -> [2]      
        System.out.println(graphM.hasEdge(1, 4));   // false
        System.out.println(graphM.hasPath(4, 2) );  // true
        graphM.addVertex(5);    // add isolated node 5 to the graph
        System.out.println(graphM.hasPath(5, 2) );  // false
        System.out.println("***"+ graphM.neighborsOf(2) ); // [1, 4]

        System.out.println("DFS:");
        graphM.dfsAll();  
        // 1 2 4 3
        // 5
    }
    static void q1_3() {
        System.out.println("Graph Node");
        GraphNode_671352 graphN = new GraphNode_671352();
        Node a = graphN.addNode(1);
        Node b = graphN.addNode(2);
        Node c = graphN.addNode(3);

        graphN.addEdge(a, b);
        graphN.addEdge(b, c);
        graphN.addEdge(a, c);

        graphN.printGraph();
            // 1 -> 2 3
            // 2 -> 1 3
            // 3 -> 2 1
        System.out.println(graphN.hasEdge(1, 3));   // true
        System.out.println(graphN.hasPath(3, 2) );  // true
        System.out.println("***"+ graphN.neighborsOf(2) ); // [1, 3]

        System.out.println("DFS:");
        graphN.dfs(a);  // 1 2 3
    }

    static void q2() {
        
        int[][] thisGraph = {{0,3,INF,INF,INF},
                                {INF,0,1,INF,INF},
                                {INF,INF,0,4,INF},
                                {INF,INF,INF,0,5},
                                {INF,INF,INF,INF,0}};
        System.out.println("computing dfs");
        q2_dfs(thisGraph);
    }

    private static void q2_dfs(int[][] thisGraph) {
        Stack<Integer> stack = new Stack<>();
        ArrayList<Integer> visited = new ArrayList<>();
        
        stack.add(0);
        while (!stack.isEmpty()) {
            int parent = stack.pop();
            visited.add(parent);
            for (int x = 0; x < thisGraph.length; x++) {
                if (0 < thisGraph[parent][x] && thisGraph[parent][x] < INF && !visited.contains(x)) { 
                    stack.add(x);
                    System.out.println("Edge " + parent + ", " + x);
                }
            }

        } // while 
        System.out.println();
    }

    static void q3_1() {
        GraphMap_671352 graphM = new GraphMap_671352();
        graphM.addEdge(1, 2);
        graphM.addEdge(2, 3);
        graphM.addEdge(2, 4);
            // 1 - 2 - 3
        System.out.println(graphM.hasCycle()); // false
    }
static void q3_2() {
    GraphMap_671352 graphM = new GraphMap_671352();
    graphM.addEdge(1, 2);
    graphM.addEdge(1, 4);
    graphM.addEdge(2, 3);
    graphM.addEdge(4,3);
        // 1 - 2
        // |   |
        // 4 - 3
    System.out.println(graphM.hasCycle());  // true
}
    static void q3_3() {
        GraphMap_671352 graphM = new GraphMap_671352();
        graphM.addEdge(1, 2);
        graphM.addEdge(2, 3);
        graphM.addEdge(4, 5);
        graphM.addEdge(5, 6);
        graphM.addEdge(4, 6);
            // 1 - 2 - 3     4 - 5 - 6 - 4      // true
        System.out.println( graphM.hasCycle() );
    }
    static void q3_4() {
        GraphMap_671352 graphM = new GraphMap_671352();
        graphM.addVertex(1);    // single node
            // 1
        System.out.println( graphM.hasCycle() );    // false
    }
}
