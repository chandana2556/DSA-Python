class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        freq={}
        threshold = len(nums)//2
        for num in nums:
            count = freq.get(num,0)+1
            freq[num]=count
            if count> threshold:
                return num
        return -1



