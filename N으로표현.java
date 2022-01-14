import java.util.*;
class Solution {
    public int solution(int N, int number) {
        int answer = 0;
        HashSet<Integer> s = new HashSet<>();
        ArrayList<HashSet<Integer>> arr = new ArrayList<>();
        for(int i=0;i<=9;i++){
            arr.add(new HashSet<Integer>());
        }
        for(int i=1;i<9;i++){
            String temp = "";
            for(int j=0;j<i;j++){
                temp += Integer.toString(N);
            }
            arr.get(i).add(Integer.parseInt(temp));
        }
        for(int i=1;i<9;i++){
            for(int j=1;j<i;j++){
                for(int x:arr.get(j)){
                    for(int y:arr.get(i-j)){
                        arr.get(i).add(x+y);
                        arr.get(i).add(x-y);
                        arr.get(i).add(x*y);
                        if(y!=0) arr.get(i).add(x/y);
                    }
                }
            }
            if(arr.get(i).contains(number)){
                answer = i;
                break;
            }
        }
        if (answer==0) answer = -1;
        return answer;
    }
}
