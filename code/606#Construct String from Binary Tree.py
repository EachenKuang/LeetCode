# https://leetcode.com/problems/construct-string-from-binary-tree/description/
class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t: return ''
        left = '({})'.format(self.tree2str(t.left)) if (t.left or t.right) else ''
        right = '({})'.format(self.tree2str(t.right)) if t.right else ''
        return '{}{}{}'.format(t.val, left, right)

    def tree2str(self, t):
	    if not t: return ""
	    subleft = "(%s)" % (self.tree2str(t.left) if t.left or t.right else "")
	    subright = "(%s)" % (self.tree2str(t.right) if t.right else "")
	    return ("%s%s%s" % (str(t.val), subleft, subright)).replace("()","")
