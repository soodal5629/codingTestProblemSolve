import java.util.*;
class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        List<List<Integer>> list = new ArrayList<>();
        for (int i = yellow ; i>0 ; i--){
            if (yellow %i == 0 && i>=yellow/i){
                List<Integer> temp = new ArrayList<>();
                temp.add(i);
                temp.add(yellow/i);
                list.add(temp);
            }
        }
        for(List<Integer> i:list){
            int w = i.get(0);
            int h = i.get(1);
            if ((w+2)*2 + (h*2) == brown){
                answer[0] = w+2;
                answer[1]= h+2;
                break;
            }
        }
        return answer;
    }
}
