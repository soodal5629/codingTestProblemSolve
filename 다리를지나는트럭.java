import java.util.*;
class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        Deque<Integer> truck = new ArrayDeque<>();
        Deque<Integer> q = new ArrayDeque<>();
        for(int i:truck_weights){
            q.add(i);
        }

        for(int i=0; i<bridge_length;i++){
            truck.add(0);
        }
        int s = 0;
        while(truck.size()>0){
            answer++;
            int temp = 0;
            if (truck.size()>0) {
                temp = truck.pollFirst();
                s-=temp;
            }
            if(q.size()>0){    
                if((s+q.peekFirst()) <= weight && truck.size()<=bridge_length){
                    s += q.peekFirst();
                    truck.add(q.pollFirst());
                }else{
                    
                    truck.add(0);
                }
            }

        }

        System.out.println(answer);
        return answer;
    }
}
