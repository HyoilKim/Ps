# my solution
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        
        result = []
        cur_s = intervals[0][0]
        cur_e = intervals[0][1]
        for i in range(len(intervals)-1):
            nxt_s = intervals[i+1][0]
            nxt_e = intervals[i+1][1]
            if cur_e >= nxt_s:
                if cur_e >= nxt_e: 
                    nxt_e = cur_e # unnecessary
                else:
                    cur_e = nxt_e
            else:
                result.append([cur_s, cur_e])
                cur_s = nxt_s
                cur_e = nxt_e
        result.append([cur_s, cur_e])
                    
        return result

# best solution
# clean code(easy understand + low variables)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged

# java solution
public int[][] merge(int[][] intervals) {
        List<int[]> res = new ArrayList<>();
        if(intervals.length == 0 || intervals == null) return res.toArray(new int[0][]);
        
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
        
        int start = intervals[0][0];
        int end = intervals[0][1];
        
        for(int[] i : intervals) {
            if(i[0] <= end) {
                end = Math.max(end, i[1]);
            }
            else {
                res.add(new int[]{start, end});
                start = i[0];
                end = i[1];
            }
        }
        res.add(new int[]{start, end});
       return res.toArray(new int[0][]);
         
    }