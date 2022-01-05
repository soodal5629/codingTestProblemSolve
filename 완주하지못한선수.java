import java.util.HashMap;
class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> hash= new HashMap<>();
        for(int i=0;i<participant.length;i++){
            if(hash.get(participant[i]) == null) hash.put(participant[i], 1);
            else hash.put(participant[i], hash.get(participant[i])+1);
         }
        for(int i=0;i<completion.length;i++){
            hash.put(completion[i], hash.get(completion[i])-1);
         }
        for (int i=0; i<participant.length; i++){
            if (hash.get(participant[i]) > 0) {
                answer = participant[i];
                break;
            }
        }
        return answer;
    }
}
