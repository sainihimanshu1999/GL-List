'''we find the median using basic recusrion formula. One thing we have to remeber if ia+ib<k then if ma>mb then 
secon part of b would not be incuded similarly if  ia+ib>k, then if ma>mb then first part of a will not be included'''

def medianTwoSorted(nums1,nums2):
    n = len(nums1)+len(nums2)

    if n%2:
        return median(nums1,nums2,n//2)

    else:
        return (median(nums1,nums2,n//2)+median(nums1,nums2,n//2-1))/2

    
def median(a,b,k):
    if not a:
        return b[k]

    if not b: 
        return a[k]

    ia,ib = len(a)//2,len(b)//2
    ma,mb = a[ia],b[ib]


    if ia+ib<k:
        if ma>mb:
            return median(a,b[ib+1:],k-ib-1)
        else:
            return median(a[ia+1:],b,k-ia-1)

    else:
        if ma>mb:
            return median(a[:ia],b,k)

        else:
            return median(a,b[:ib],k)


nums1 = [1,2]
nums2 = [3,4]

print(medianTwoSorted(nums1,nums2))
