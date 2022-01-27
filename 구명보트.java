import java.util.*;
class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        int left = 0;
        int right = people.length-1;
        Arrays.sort(people);
        while(left<=right){
            if (people[right]+people[left] <= limit) {
                answer++;
                right--;
                left++;
            }
            else if(right == left){
                answer ++;
                break;
            }
            else{
                right--;
                answer++;
            }
        }
        return answer;
    }
}
