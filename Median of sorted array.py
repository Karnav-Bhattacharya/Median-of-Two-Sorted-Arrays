class Solution:
    def median(self, nums1: list[int], nums2: list[int]) -> float:
        lst = nums1 + nums2
        lst.sort()
        n = len(lst)
        if n%2 == 0:
            return float((lst[int(n/2)-1] + lst[int((n/2)+1)-1])/2)

        else:
            return float(lst[int(n/2)])

answer = Solution()
print(answer.median(nums1=[1, 3], nums2=[2]))
# print()
