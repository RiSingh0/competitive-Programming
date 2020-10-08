class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L,R = 0,len(nums)-1
        while L <= R:
            M = (L+R)//2
            Lpos = nums[L]
            Mpos = nums[M]
            Rpos = nums[R]
            if target == Mpos:
                return M
            if Lpos <= Mpos:
                if Lpos <= target and target <= Mpos:
                    R = M-1
                else:
                    L = M+1
            elif Mpos <= Rpos:
                if Mpos <= target and target <= Rpos:
                    L = M+1
                else:
                    R = M-1
        return -1
