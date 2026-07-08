class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        res = []
        i= 0
        while i < n:
            j = i + 1
            k = n-1
            while j < k:
                summ = nums[i] + nums[j] + nums[k]
                if summ == 0:
                    res.append([nums[i],nums[j],nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j+=1
                    while k > j and nums[k] == nums[k-1]:
                        k -= 1
                    
                    j += 1
                    k -= 1
                elif summ > 0:
                    while k > j and nums[k] == nums[k-1]:
                        k -= 1
                    k -= 1

                else:
                    while j < k and nums[j] == nums[j+1]:
                        j+=1
                    j+=1
            while i < n-1 and nums[i] == nums[i+1]:
                i += 1
            i+= 1


        return res            
                    

