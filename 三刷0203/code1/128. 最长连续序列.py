class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums.sort()

        # mp=collections.defaultdict(int)

        # for i in nums:
        #     mp[i]=1

        # n=len(nums)

        # i=0

        # ans=0
        # count=1
        # while i<n:

        #     if mp[nums[i]+1]==1:
        #         count+=1
        #         i+=1
        #         while i<n and nums[i]==nums[i-1]:
        #             i+=1

        #         ans=max(ans,count)

        #     else:
        #         count=1
        #         i+=1

        # return ans

        st=set(nums)
        ans=0

        for num in st:
            if num-1 in st:
                continue

            begin=num

            while begin+1 in st:
                begin+=1

            ans=max(ans,begin-num+1)

        return ans
            
