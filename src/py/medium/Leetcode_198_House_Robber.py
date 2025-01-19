class Solution:
    def rob(self, nums: List[int]) -> int:

        # if len(nums) <2 :
        #     return nums[0]

        # dp_list=[0]*len(nums)
        # dp_list[0]=nums[0]
        # dp_list[1]=max(nums[1],nums[0])

        # i=2
        # while i<len(nums):
        #     #print(i,dp_list,dp_list[i-2],nums[i],nums[i-1])
        #     dp_list[i]= max( (dp_list[i-2] + nums[i]) , dp_list[i-1] )
        #     #print(dp_list)
        #     i+=1

        # return dp_list[i-1]

        
        n=len(nums)-1
        dp={}

        def recusive_call(i,nums,dp):

            if i==0:
                return nums[0]
            if i==-1:
                return 0
            if i in dp:
                return dp[i]

            dp[i]=max(recusive_call(i-1,nums,dp), recusive_call(i-2,nums,dp)+ nums[i])
            return dp[i]

        return recusive_call(n,nums,dp)
