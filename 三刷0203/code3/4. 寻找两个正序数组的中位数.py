class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m,n=len(nums1),len(nums2)

        def getmk(k):

            index1,index2=0,0

            while True:

                if index1==m:
                    return nums2[index2+k-1]

                if index2==n:
                    return nums1[index1+k-1]

                newindex1=min(index1+k//2-1,m)
                newindex2=min(index2+k//2-1,n)

                if nums1[newindex1]<nums2[newindex2]:
                    k-=newindex1-index1-1
                    index1=newindex1
                else:
                    k-=newindex2-index2-1
                    index2=newindex2
            
        if (m+n)%2==0:
            return (getmk((m+n)//2)+getmk((m+n)//2+1))/2
        else:
            return getmk((m+n+1)//2)