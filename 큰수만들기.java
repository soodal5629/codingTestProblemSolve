import java.util.*;
class Solution {
    public String solution(String number, int k) {
        String answer = "";
        ArrayList<Integer> arr = new ArrayList<>();
        for(int i=0;i<number.length();i++){
            arr.add(Integer.parseInt(number.substring(i,i+1)));
        }
        Deque<Integer> temp = new ArrayDeque<>();
        
        for(int i=0;i<arr.size();i++){
            while(k>0 && temp.size()>0 && temp.peekLast()<arr.get(i)){
                k--;
                temp.pollLast();
            }
            temp.add(arr.get(i));
        }
     
        while(temp.size()>0){
            answer += temp.pollFirst();
        }
        if(k>0) answer = answer.substring(0, k+1);
        return answer;
    }
}
