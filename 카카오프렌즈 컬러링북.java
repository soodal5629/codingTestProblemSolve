import java.util.*;
class Solution {
    public int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;
        int [][] map = new int[m][n];
        for(int i=0;i<m;i++){
            for (int j=0;j<n;j++){
                map[i][j] = picture[i][j];
            }
        }
        for(int i=0;i<m;i++){
            for (int j=0;j<n;j++){
                if (map[i][j] == 0) continue;
                else{
                    numberOfArea++;
                    maxSizeOfOneArea = Math.max(dfs(map,i,j), maxSizeOfOneArea);
                }
            }
        }

        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }
    static public int dfs(int [][] picture, int x, int y){
        int [] dx = {-1,1,0,0};
        int [] dy = {0,0,-1,1};
        int m = picture.length;
        int n = picture[0].length;
        int temp = 0;
        Deque<ArrayList<Integer>> d= new ArrayDeque<>();
        ArrayList<Integer> list = new ArrayList<>();
        list.add(x);
        list.add(y);
        d.add(list);
        int value = picture[x][y];
        while(d.size()>0){
            ArrayList<Integer> arr = d.removeFirst();
            x = arr.get(0);
            y = arr.get(1);
            for(int i =0;i<4;i++){
                int index_x = x+dx[i];
                int index_y = y+dy[i];
                if (index_x<0 || index_y<0 || index_x>=m || index_y >= n) continue;
                else if(picture[index_x][index_y]==value){
                    picture[index_x][index_y] = 0;
                    temp++;
                    ArrayList<Integer> list2 = new ArrayList<>();
                    list2.add(index_x);
                    list2.add(index_y);
                    d.add(list2);
                }
            }
        }
        return temp;
    }
}
