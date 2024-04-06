import java.util.*;

class Solution {   
    public String output(int[] scoreArr) {
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
        int[] scores = {0, 0, 0, 0};
        
        for (int i=0; i < survey.length; i++) {
            char first = survey[i].charAt(0);
            int score = (4 - choices[i]);
            int idx = 0;
            
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
