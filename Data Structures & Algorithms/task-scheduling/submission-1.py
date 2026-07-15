class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxFreq = max(count.values())
        maxCount = sum([1 if v == maxFreq else 0 for v in count.values()])

        return max(len(tasks), (maxFreq-1)*(n+1) + maxCount)