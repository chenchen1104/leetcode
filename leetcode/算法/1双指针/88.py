m = 1
n = 1
nums1 = [2, 0]
nums2 = [1]
index1 = m - 1
index2 = n - 1
indexmerge = m + n - 1
while index2 >= 0:
    if index1 < 0:
        nums1[indexmerge] = nums2[index2]
        index2 -= 1
        indexmerge -= 1
    elif index2 < 0:
        nums1[indexmerge] = nums1[index1]
        index1 -= 1
        indexmerge -= 1
    elif nums1[index1] >= nums2[index2]:
        nums1[indexmerge] = nums1[index1]
        index1 -= 1
        indexmerge -= 1
    elif nums1[index1] < nums2[index2]:
        nums1[indexmerge] = nums2[index2]
        index2 -= 1
        indexmerge -= 1
