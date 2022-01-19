import java.util.*;
class Solution {
    public int[] solution(int[] prices) {
        Deque<Integer> q = new ArrayDeque<>();
        for(int i:prices){
            q.add(i);
        }
        ArrayList<Integer> arr = new ArrayList<>();
        while(q.size()>0){
            int now = q.pollFirst();
            int cnt = 0;
            for(int i:q){
                cnt++;
                if (now>i) break;
            }
            arr.add(cnt);
        }
        int[] answer = new int[arr.size()];
        for (int i=0; i<arr.size();i++){
            answer[i] = arr.get(i);
        }
        return answer;
    }
}
