class Solution:
    def arrangeCoins(self, n: int) -> int:
        # stair_no=1
        # n-=1
        # while n >= stair_no+1:
        #     #print(f"Coins Left = {n} and Stair Count = {stair_no}")
        #     stair_no+=1
        #     n=n-stair_no

        # return stair_no

        left=0
        right=n

        while left <=right:

            mid= (left + right) //2 

            coins= mid * (mid + 1) //2

            if coins == n:
                return mid
            elif coins>n:
                right=mid-1
            else:
                left=mid+1
        return right



