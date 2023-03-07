import java.util.*;
class Solution {
public static int bfs(int[][] board, int x, int y, int value) {
        Deque<List<Integer>> d = new ArrayDeque<>();
        List<Integer> temp = new ArrayList<>();
        temp.add(x); 
        temp.add(y);
        d.add(temp);
        int cnt = 0;
        //int value = picture[x][y];
        board[x][y] = 0;
        int [] dx = {-1,1,0,0};
        int [] dy = {0,0,-1,1};
        while(d.size() > 0) {
            List<Integer> now = d.poll();
            cnt++;
            int i = now.get(0);
            int j = now.get(1);
            
            for(int k = 0;k<4;k++) {
                int di = i+dx[k];
                int dj = j+dy[k];
                if(di <0 || dj <0 || di >= board.length || dj>=board[0].length) continue;
                if(board[di][dj] == value) {
                    List<Integer> temp2 = new ArrayList<>();
                    temp2.add(di);
                    temp2.add(dj);
                    d.add(temp2);
                    board[di][dj] = 0;
                }
            }
            
        }
        return cnt;
    }
    
    public int[] solution(int m, int n, int[][] picture) {
        int[][] board = new int[m][n];
        for(int i = 0; i<m; i++){
            for(int j=0; j<n;j++){
                board[i][j] = picture[i][j];
            }
        }
        
        int maxSizeOfOneArea = 0;
        int[] answer = new int[2];
        int count = 0;
        
        for(int i = 0; i < m; i++){
            for(int j=0; j< n;j++){
                if(board[i][j] != 0){
                    count++;
                    maxSizeOfOneArea = Math.max(maxSizeOfOneArea, bfs(board, i, j, board[i][j]));
                }
            }
        }
        answer[0] = count;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }
}
