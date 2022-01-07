import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

class Main {
    static HashMap<String, Boolean> cache = new HashMap<>();
    static Queue<Node> q = new LinkedList<>();
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int s = scanner.nextInt();
        scanner.close();

        System.out.println(bfs(1,s));
    }

    private static int bfs(int start, int end) {
        int result = 0;

        q.add(new Node(start, 0));

        while (!q.isEmpty()) {
            int size = q.size();

            for (int i=0; i<size; i++) {
                Node node = q.poll();
                if (node.s == end) return result;

                copyAll(node);
                paste(node);
                deleteOne(node);
            }

            result++;
        }

        return result;
    }

    private static void copyAll(Node node) {        
        Node result = new Node(node.s, node.s);
        String key = result.toString();
        if (cache.containsKey(key)) return;

        cache.put(key, true);
        q.add(result);
    }

    private static void paste(Node node) {
        Node result = new Node(node.s+node.c, node.c);
        String key = result.toString();
        if (cache.containsKey(key)) return;

        cache.put(key, true);
        q.add(result);
    }

    private static void deleteOne(Node node) {
        Node result = new Node(node.s-1, node.c);
        String key = result.toString();
        if (cache.containsKey(key)) return;

        cache.put(key, true);
        q.add(result);
    }
}

class Node {
    int s,c;
    public Node(int s, int c) {
        this.s = s;
        this.c = c;
    }

    @Override
    public String toString() {
        return String.format("%s %s", s, c);
    }
}