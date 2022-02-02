class Solution {
    static int cnt =0;
    static public void dfs(int idx, int value, int[] numbers, int target){
        if(idx == numbers.length){
            if (value == target){
                cnt++;
            }
            return;
        }
        dfs(idx+1, value+numbers[idx], numbers, target);
        dfs(idx+1, value-numbers[idx], numbers, target);
    }
    public int solution(int[] numbers, int target) {
        int answer = 0;
        dfs(0,0, numbers, target);
        answer = cnt;
        return answer;
    }
}
