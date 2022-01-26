import java.util.*;
class Solution {
    public int solution(String numbers) {
        int answer = 0;
         Set<Integer> set = new HashSet<>();
        int n = numbers.length();
        String[] arr = new String[n];
        for(int i = 0;i <n ; i++){
            arr[i] = numbers.substring(i,i+1);
        }
        for (int i=1;i<=n;i++){
            String [] output = new String[i];
            perm(n, arr, set, 0, i, output);
        }
        
        Iterator<Integer> it = set.iterator();
        while(it.hasNext()){
           int num = it.next();
           System.out.println(num);
           if(num == 0 || num == 1) continue;
           else if(num == 2||num == 3||num == 5) answer++;
           else{
               boolean flag = false;
               for(int i = 2; i<= num/2; i++){       
                   if(num % i == 0){
                       flag = true;
                       break;
                   }
               }
               if (!flag) answer ++;
           }
        }
        return answer;
    }
    static public void perm(int n, String[] arr, Set<Integer> set, int depth, int r, String[] output){ // 순열 구현 
        if (depth == r) {
            String temp = "";
            for(int i=0;i<output.length;i++){
                temp += output[i];
            }
            set.add(Integer.parseInt(temp));
            return;
        }
        for(int i=0;i<n;i++){
            if(arr[i].equals("")) continue;
            output[depth] = arr[i];
            String temp = arr[i];
            arr[i] = "";
            perm(n, arr, set, depth+1,r, output);
            arr[i] = temp;   
        }    
    }
}
