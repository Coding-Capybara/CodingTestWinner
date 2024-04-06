import java.util.*;

class Solution {   
    public String output(int[] scoreArr) {
        // 계산된 스코어에 따라 지표를 결정해주는 function
        // String으로 된 정답을 return 해줌
        String ans = "";
        
        if (scoreArr[0] >= 0) ans += "R";
        else if (scoreArr[0] < 0) ans += "T";
        
        if (scoreArr[1] >= 0) ans += "C";
        else if (scoreArr[1] < 0) ans += "F";
        
        if (scoreArr[2] >= 0) ans += "J";
        else if (scoreArr[2] < 0) ans += "M";
        
        if (scoreArr[3] >= 0) ans += "A";
        else if (scoreArr[3] < 0) ans += "N";
        
        return ans;
    }
    
    public String solution(String[] survey, int[] choices) {
        // 각 지표의 점수를 받을 수 있는 scores array를 initialize
        int[] scores = {0, 0, 0, 0};
        
        // survey를 for loop으로 돌면서 점수 계산
        for (int i=0; i < survey.length; i++) {
            char first = survey[i].charAt(0); // 각 survey의 왼쪽 character 받기
            int score = (4 - choices[i]); // 업데이트 해줄 점수 받기 (왼쪽은 positive, 오른쪽은 negative)
            int idx = 0; // 업데이트 해줄 인덱스
            
            // 만약 survey가 RT라면 positive는 R에 점수를 주고, negative는 T에 점수를 줘야함
            // 하지만 survey가 TR로 들어오면 positive -> T, negative -> R이 되어버림
            // 기준을 유지하기 위해 first가 T면 -1을 곱해주기로 함
            if (survey[i].contains("R")) {
                idx = 0;
                if (first == 'T') score *= -1;
            }
            else if (survey[i].contains("C")) {
                idx = 1;
                if (first == 'F') score *= -1;
            }
            else if (survey[i].contains("J")) {
                idx = 2;
                if (first == 'M') score *= -1;
            }
            else if (survey[i].contains("A")) {
                idx = 3;
                if (first == 'N') score *= -1;
            }
            
            scores[idx] += score;        
        }
                
        return output(scores);
    }
}
