package Lab12ab.pack;
import java.util.Map;
import java.util.List;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Set;
import java.util.HashSet;

public class GraphMap_671352 {
    private Map<Integer, List<Integer>> graph;

    public GraphMap_671352() {
        graph = new HashMap<>();
    }

    public void addVertex(int v) {
        graph.putIfAbsent(v, new ArrayList<>());
    }

    public void addEdge(int src, int dest) {
        graph.putIfAbsent(src, new ArrayList<>());
        graph.putIfAbsent(dest, new ArrayList<>());
        graph.get(src).add(dest);
        graph.get(dest).add(src); // remove if directed
    }
    
    public List<Integer> neighborsOf(int i) {
        if (graph.containsKey(i)) {
            return graph.get(i);
        }
        System.out.println("out of range"); 
        return Collections.emptyList();
    }

    public boolean hasEdge(int n1, int n2) {
        if (!graph.containsKey(n1) || !graph.containsKey(n2)) {
            return false;
        }
        return graph.get(n1).contains(n2);
    }

    public boolean hasPath(int n1, int n2) {
        if (!graph.containsKey(n1) || !graph.containsKey(n2)) {
            return false;
        }
        Set<Integer> visited = new HashSet<>();
        return hasPathDFS(n1, n2, visited);
    }

    private boolean hasPathDFS(int current, int target, Set<Integer> visited) {
        if (current == target) return true;
        visited.add(current);

        for (int neighbor : graph.get(current)) {
            if (!visited.contains(neighbor)) {
                if (hasPathDFS(neighbor, target, visited)) {
                    return true;
                }
            }
        }
        return false;
    }

    public void dfs(int src) {
        if (!graph.containsKey(src)) {
            System.out.println("Error: Node " + src + " does not exist in this graph.");
            return;
        }
        Set<Integer> visited = new HashSet<>();
        dfsHelper(src, visited);
        System.out.println("");
    }

    private void dfsHelper(int v, Set<Integer> visited) {
        visited.add(v);
        System.out.print(v + " ");

        for (int neighbor : graph.get(v)) {
            if (!visited.contains(neighbor)) {
                dfsHelper(neighbor, visited);
            }
        }
    }

    public void dfsAll() {
        Set<Integer> visited = new HashSet<>();
        for (int v : graph.keySet()) {
            if (!visited.contains(v)) {
                dfsHelper(v, visited);
                System.out.println(); // newline after each component
            }
        }
    }    

    public void printGraph() {
        for (int v : graph.keySet()) {
            System.out.println(v + " -> " + graph.get(v));
        }
    }
public boolean hasCycle() {
    Set<Integer> visited = new HashSet<>();

    for (int v : graph.keySet()) {
        if (!visited.contains(v)) {
            if (hasCycleDFS(v, -1, visited)) {
                return true;
            }
        }
    }
    return false;
}

private boolean hasCycleDFS(int current, int parent, Set<Integer> visited) {
    visited.add(current);

    for (int neighbor : graph.get(current)) {
        if (!visited.contains(neighbor)) {
            // explore deeper
            if (hasCycleDFS(neighbor, current, visited)) {
                return true;
            }
        } else if (neighbor != parent) {
            // found a back edge -> cycle
            return true;
        }
    }
    return false;
}  
}
