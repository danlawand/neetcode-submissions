class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # median = (m+n)//2
        m = len(nums1) 
        n = len(nums2)
        # if (n+m)%2 == 2: ceil((n+m)/2) + (n+m)//2
        p1 = 0
        p2 = 0
        median1 = 0
        median2 = 0
        countToMedian = 1
        maxToMedian = ((n+m)//2)+1
        while countToMedian <= maxToMedian:
            countToMedian += 1
            if p1 >= m:
                median2 = median1
                median1 = nums2[p2]
                p2 += 1
                continue
            if p2 >= n:
                median2 = median1
                median1 = nums1[p1]
                p1 += 1 
                continue               
            if nums1[p1] <= nums2[p2]:
                median2 = median1
                median1 = nums1[p1]
                p1 += 1
            else:
                median2 = median1
                median1 = nums2[p2]
                p2 += 1

        oddOrEven = (m+n)%2
        if oddOrEven == 0:
            return (median2+median1)/2
        return median1


