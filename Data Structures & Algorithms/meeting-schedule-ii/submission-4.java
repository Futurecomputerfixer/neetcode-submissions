/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

class Solution {
    public int minMeetingRooms(List<Interval> intervals) {
        int cnt = 0;
        int[] start = new int[intervals.size()];
        int[] end = new int[intervals.size()];
        for(int i = 0; i < intervals.size(); i++){
            start[i] = intervals.get(i).start;
            end[i] = intervals.get(i).end;
        }

        Arrays.sort(start);
        Arrays.sort(end);

        int i = 0, j = 0;

        while(i < intervals.size()){
            if(start[i] < end[j]) i++;
            else j++;
            cnt = Math.max(cnt, i - j);
        }
        return cnt;
    }
}
