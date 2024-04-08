import java.util.*;

class Solution {
    public int[] solution(int k, int[] score) {
        ArrayList<Integer> ans = new ArrayList<>();
        PriorityQueue<Integer> topk = new PriorityQueue<>();
        
        for (int num : score){
            // 자바의 PriorityQueue의 길이는 .size()로
            if (topk.size() < k) {
                topk.add(num);
            }
            else {
                // .peek()은 가장 작은 값 (첫번째 값)을 반환
                // .poll()은 가장 작은 값을 제거 후 반환, 비었다면 null 반환
                if (num > topk.peek()) {
                    topk.poll();
                    topk.add(num);
                }
            }
            ans.add(topk.peek());
        }
        
        // ArrayList<Integer> -> int[]
        int[] result = ans.stream().mapToInt(i -> i).toArray();
        return result;
    }
}