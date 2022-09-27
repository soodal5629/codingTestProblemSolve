import java.util.Deque;
import java.util.ArrayDeque;
class Solution {
    boolean solution(String s) {
        boolean answer = true;
        Deque<Character> d = new ArrayDeque<>();
        
        for(int i = 0; i<s.length(); i++) {
            
            if (d.size() == 0){
                d.add(s.charAt(i));
                continue;
            }
            char top = d.peekLast();
            if(top == s.charAt(i)){
                d.add(s.charAt(i));
                continue;
            }else if(top == '(' && s.charAt(i) == ')'){
                d.pop();
                continue;
            }
        }
        if(d.size()>0) answer = false;

        return answer;
    }
}
