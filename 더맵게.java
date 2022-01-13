import java.util.*;
class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> q= new PriorityQueue<>();
        Arrays.stream(scoville).forEach(s-> q.add(s));
        int first = q.poll();
        while(first<K && q.size()>0){
            int mix = first+(q.poll()*2);
            q.add(mix);
            answer++;
            first = q.poll();               
        }
        if (first<K) answer = -1;
        
        return answer;
    }
}
