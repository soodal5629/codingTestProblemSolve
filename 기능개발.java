import java.util.*;
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> list = new ArrayList<>();
        Deque<Integer> time = new ArrayDeque<>();
        Deque<Integer> q= new ArrayDeque<>();
        for (int i=0; i<progresses.length; i++){
            int temp  = (int)Math.ceil((double)(100-progresses[i])/speeds[i]);
            time.add(temp);
        }
        if (time.size() == 1){
            list.add(time.getFirst());
        }else{
            q.add(time.pollFirst());
            while (time.size()>0){
                int q_bottom = q.getFirst();
                int push = time.pollFirst();
                if (q_bottom >= push){
                    q.add(push);
                }else{
                    list.add(q.size());
                    q.clear();
                    q.add(push);
                }
            }
            if(q.size()>0) list.add(q.size());
        }
        
        int[] answer = new int[list.size()];
        for(int i = 0; i < list.size(); i++) answer[i] = list.get(i);
        return answer;
    }
}
