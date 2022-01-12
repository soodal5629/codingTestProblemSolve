import java.util.*;
class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        ArrayList<Integer> arr = new ArrayList<>();
        for(int i=0; i<numbers.length;i++){
            arr.add(numbers[i]);
        }
        arr.sort((Integer n1, Integer n2) -> {
            String temp1 = "";
            String temp2 = "";
            for(int i=0;i<4;i++){
                temp1 +=Integer.toString(n1);
                temp2 += Integer.toString(n2);
            }
            temp1 = temp1.substring(0,4);
            temp2 = temp2.substring(0,4);
            if (Integer.parseInt(temp1)>Integer.parseInt(temp2)) return -1;
            else if(Integer.parseInt(temp1)==Integer.parseInt(temp2)) return 0; // 이 조건문 안쓰면 런타임에러 발생함.. 왜인지는 아직 잘 모르겟음
            else return 1;
        });
        for(int i=0; i<arr.size(); i++){
            answer += Integer.toString(arr.get(i));
        }
        if (answer.charAt(0)=='0') answer = "0";
        return answer;
    }
}
