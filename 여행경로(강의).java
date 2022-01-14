import java.util.*;
class Solution {
    public String[] solution(String[][] tickets) {
        String[] answer = {};
        Map<String, ArrayList<String>> routes = new HashMap<>();

        for(int i=0; i<tickets.length;i++){
            if(routes.get(tickets[i][0]) == null){
                routes.put(tickets[i][0], new ArrayList<String>());
            }
            routes.get(tickets[i][0]).add(tickets[i][1]);
        }

        for(String i : routes.keySet()){
            routes.get(i).sort(Collections.reverseOrder());
        }

        List<String> path = new ArrayList<>();
        Deque<String> stack = new ArrayDeque<>();
        stack.add("ICN");
        while(stack.size()>0){
            String now = stack.peekLast();
            if(routes.get(now) == null || routes.get(now).size() == 0){
                path.add(stack.pollLast());
            }else{
                int temp = routes.get(now).size();
                stack.add(routes.get(now).remove(temp-1));
            }
        }
        List<String> temp2 = new ArrayList<>();
        
        for(int i=path.size()-1;i>=0;i--){
            temp2.add(path.get(i));
        }
        answer =temp2.toArray(new String[temp2.size()]);
        return answer;
    }
}
