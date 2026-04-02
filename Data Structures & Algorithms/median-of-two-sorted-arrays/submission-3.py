class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        median = -1
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        n = len(nums1)
        m = len(nums2)
        if n==0:
            if m%2==0:
                return float(nums2[m//2]+nums2[m//2-1])/2
            else:
                return float(nums2[m//2])
        total = n+m
        l, r = 0, n
        needed = total//2-1 if total%2==0 else total//2
        mid, pos = -1, 0
        print(f"nums1:{nums1}\nnums2:{nums2}\nNeeded count on left:{needed}")
        while l<r:
            mid = (l+r)//2
            pos = -1
            print(f"nums1 l:{l} r:{r} mid:{mid}")
            lm, rm = 0, m
            while lm<rm:
                midm = (lm+rm)//2
                if nums2[midm] < nums1[mid]:
                    lm = midm+1
                else:
                    rm = midm
            if pos == -1:
                pos = lm
            print(f"Pos found in nums2:{pos}")
            if needed <= mid+pos <= needed + (1 if total%2==0 else 0):
                print(f"\nFound! with mid{mid} and pos{pos}")
                if total%2 == 0:
                    if mid+pos == needed:
                        print(f"Logic 1")
                        first_elem = nums1[mid]
                        second_elem = min(nums1[mid+1] if mid+1<n else float('inf'), nums2[pos])
                        median = float(first_elem+second_elem)/2
                    else:
                        print(f"Logic 2")
                        first_elem = nums1[mid]
                        second_elem = max(nums1[mid-1] if mid>0 else -1, nums2[pos-1] if pos>0 else -1)
                        median = float(first_elem+second_elem)/2
                    break
                else:
                    median = nums1[mid]
                    break
            elif mid+pos > needed:
                print(f"its {mid+pos-needed} more than we need")
                r = mid
            else:
                print(f"its {needed-(mid+pos)} less than we need")
                l = mid+1
        if median == -1:
            print("Yeah man, not even single median was in smaller array, but atleast we have strong idea")
            delta = needed-(mid+pos)
            print(f"We have delta of {delta} and we just go there in secodn elem")
            if total%2 == 0:
                median = 4
            else:
                median = nums2[pos+delta]
        print(f"F mate! mid was {mid} and pos was {pos}")
        return median
        