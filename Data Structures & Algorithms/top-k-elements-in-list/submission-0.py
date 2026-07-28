class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        topK = sorted(list(count.items()), key = lambda x: x[1], reverse=True)
        return [item[0] for item in topK[:k]]
            