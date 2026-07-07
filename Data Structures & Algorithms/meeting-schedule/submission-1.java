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
    public boolean canAttendMeetings(List<Interval> intervals) {
        Collections.sort(intervals, (
            (Interval i1, Interval i2) -> Integer.compare(i1.start, i2.start)));
        int start = 0, end = 0;
        for(Interval i : intervals){
            if(start == end && end == 0) //init
                end = i.end;
            else{
                start = i.start;
                if(start < end) return false;
                end = i.end;
            }
        }
        return true;
    }
}
