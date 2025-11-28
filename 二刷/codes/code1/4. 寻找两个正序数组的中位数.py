from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m,n=len(nums1),len(nums2)



        def getans(k):

            index1, index2 = 0, 0

            while True:
                if index1 == m:
                    return nums2[index2 + k - 1]
                if index2 == n:
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])

                newindex1, newindex2 = min(index1 + k // 2 - 1, m - 1), min(index2 + k // 2 - 1, n - 1)

                num1, num2 = nums1[newindex1], nums2[newindex2]
                if num1 > num2:
                    k -= newindex2 - index2 + 1
                    index2 = newindex2 + 1
                else:
                    k -= newindex1 - index1 + 1
                    index1 = newindex1 + 1

        if (m+n)%2==1:
             return getans((m+n+1)//2)
        else:
            return (getans((m+n)//2)+getans((m+n)//2+1))/2