import java.util.Scanner;

class Main {

    private static Scanner sc = new Scanner(System.in);
    
    public static void main(String[] args) {

        int n = sc.nextInt();
        int[][] g = new int[n][n];

        mapInput(g);
        floydWarshall(g);
        System.out.print(getOutput(g));
    }

    private static void mapInput(int[][] g) {
        for (int i=0; i < g.length; i++) {
            for (int j=0; j < g.length; j++) {
                g[i][j] = sc.nextInt();
            }
        }
    }

    private static void floydWarshall(int[][] g) {
        for (int k=0; k < g.length; k++) {
            for (int i=0; i < g.length; i++) {
                for (int j=0; j < g.length; j++) {
                    if (g[i][j] == 1) continue;
                    if (g[i][k] + g[k][j] != 2) continue;
                    g[i][j] = 1;
                }
            }
        }
    }

    private static StringBuilder getOutput(int[][] g) {

        StringBuilder sb = new StringBuilder();

        for (int i=0; i < g.length; i++) {
            for (int j=0; j < g.length; j++) {
                sb.append(String.format("%d ", g[i][j]));
            }
            sb.append('\n');
        }

        return sb;
    }
}