# https://leetcode.com/problems/reverse-string-ii/description/
class Solution:
	# 1 使用切片
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        for i in range(0, len(s), 2*k):
            s[i:i+k] = reversed(s[i:i+k])
        return "".join(s)
    # 2
    def reverseStr(self, s, k):
    	s = list(s[0+i:k+i] for i in range(0,len(s),k))
        output = []
        for j in range(len(s)):
            if j % 2 == 0:
                output.append(s[j][::-1])
            else:
                output.append(s[j])
        return "".join(output)