import java.util.*;
class Solution {
    static public int find(int x, int [] parent){
        if (x != parent[x]){
            parent[x] = find(parent[x], parent);
        }
        return parent[x];
    }
    static public int[] union(int a, int b, int [] parent){
        a = find(a, parent);
        b = find(b, parent);
        if (b>a) parent[b] = a;
        else parent[a] = b;
        return parent;
    }
    public int solution(int n, int[][] costs) {
        int answer = 0;
        List<ArrayList<Integer>> q= new ArrayList<>();
        Arrays.sort(costs, (a,b)-> Integer.compare(a[2],b[2]));
        for (int [] i : costs){
            ArrayList<Integer> temp = new ArrayList<>();
            temp.add(i[2]);
            temp.add(i[0]);
            temp.add(i[1]);
            q.add(temp);
        }
        int [] parent = new int[n];
        for(int i=0; i<n;i++){
            parent[i] = i;
        }
        for(int i=0; i<costs.length;i++){
            int cost = q.get(i).get(0);
            int a = q.get(i).get(1);
            int b = q.get(i).get(2);
            System.out.println(cost+" "+a+" "+b);
            if (find(a, parent) != find(b, parent)){
                System.out.println("ㅇㅇㅇ");
                union(a,b,parent);
                answer += cost;
            }
            
        }
        return answer;
    }
    
}
