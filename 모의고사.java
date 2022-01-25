import java.util.*;
class Solution {
    public int[] solution(int[] answers) {
        int [] first = {1,2,3,4,5};
        int[] second = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] third= {3,3,1,1,2,2,4,4,5,5};
    
        int cnt1 =0, cnt2 = 0, cnt3=0;
        for(int i =0 ;i<answers.length;i++){
            if (first[i%first.length] == answers[i]) cnt1 +=1;
            if (second[i%second.length] == answers[i]) cnt2 +=1;
            if (third[i%third.length] == answers[i]) cnt3 +=1;
        }
        int [] arr = {cnt1,cnt2,cnt3};
        int maxi = -1;
        for (int i=0;i<3;i++){
            if (maxi < arr[i]){
                maxi = arr[i];
            }
        }
        
        ArrayList<Integer> list = new ArrayList<>();
        for (int i=0;i<3;i++){
            if (maxi == arr[i]){
                list.add(i+1);
            }
        }
        int[] answer=new int[list.size()];
        for (int i=0;i<list.size();i++){
            answer[i] = list.get(i);
        }
        return answer;
    }
}
