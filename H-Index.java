import java.util.*;
class Solution {
    public int solution(int[] citations) {
        int answer = 0;
       Arrays.sort(citations);
       int n = citations.length;
       for (int i=0;i<=citations.length;i++){ // input이 {5,5,5,5} 일 경우, 4 return
           int index = 0;
           boolean flag = false;
           for (int j = 0; j<citations.length;j++){
               if (citations[j]>=i){
                   index = j;
                   flag = true;
                   break;
               }
           }
           if (flag && n-index>=i){
               answer = Math.max(answer, i);
           }
       }
        return answer;
    }
}
