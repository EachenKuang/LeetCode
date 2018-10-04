# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def helper(nums,start,end):
            if start>=end:
                return None
            mid = start+(end-start)//2
            parent = TreeNode(nums[mid])
            parent.left = helper(nums,start,mid)
            parent.right = helper(nums,mid+1,end)
            return parent
        return helper(nums,0,len(nums))