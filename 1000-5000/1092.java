import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        Integer[] cranes = new Integer[n];

        for (int i=0; i<n; i++) {
            cranes[i] = scanner.nextInt();
        }

        int m = scanner.nextInt();
        Integer[] boxes = new Integer[m];

        for (int i=0;i<m;i++) {
            boxes[i] = scanner.nextInt();
        }

        scanner.close();

        Arrays.sort(cranes, Collections.reverseOrder());
        Arrays.sort(boxes, Collections.reverseOrder());
        
        int[] counts = new int[n];

        System.out.println(solve(cranes, boxes, counts));
    }

    private static int solve(Integer[] cranes, Integer[] boxes, int[] counts) {
        if (cranes[0] < boxes[0]) {
            return -1;
        }

        for (Integer box: boxes) {
            serveBox(cranes, box, counts);
        }

        return getMaxCount(counts);
    }

    private static int getMaxCount(int[] counts) {
        int result = 0;

        for (int count: counts) {
            if (count < result) continue;
            result = count;    
        }

        return result;
    }

    private static void serveBox(Integer[] cranes, Integer box, int[] counts) {
        int candidate = 0;

        for (int i=0; i<cranes.length; i++) {
            Integer crane = cranes[i];
            if (crane < box) continue;
            if (counts[candidate] < counts[i]) continue;

            candidate = i;
        }

        counts[candidate]++;
    }
}