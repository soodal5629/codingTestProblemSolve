import java.util.*;
class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        Deque<ArrayList<Integer>> d = new ArrayDeque<>();
        int cnt = 0;
        for(int i : priorities){
            ArrayList<Integer> arr = new ArrayList<>();
            arr.add(cnt);
            arr.add(i);
            d.add(arr);
            cnt++;
        }
        while(d.size()>0){
            ArrayList<Integer> now = d.pollFirst();
            int maxi = -1;
            Iterator<ArrayList<Integer>> i = d.iterator();
            while(i.hasNext()){
                int temp= i.next().get(1);
                if(temp > maxi) maxi = temp;    
            }
            if(now.get(1) < maxi){
                d.add(now);
            }else{
                answer++;
                if(location == now.get(0)) break;
            }
            
        }
        return answer;
    }
}
