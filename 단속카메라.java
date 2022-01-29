import java.util.*;
class Solution {
    public int solution(int[][] routes) {
        int answer = 1;
        Arrays.sort(routes, (num1, num2)-> Integer.compare(num1[1], num2[1])); // 2차원배열 두번째 키값을 기준으로 오름차순 정렬
  
        int camera = routes[0][1];
        for (int i=1; i<routes.length;i++){
            if (camera<routes[i][0]){
                camera = routes[i][1];
                answer++;
            }
        }
        return answer;
    }
}
