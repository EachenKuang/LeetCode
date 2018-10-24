# https://leetcode.com/problems/longest-palindrome/description/
class Solution:
    # 1 使用字典来计数
    # 长度为一个奇数加上偶数个字母
    # 字母个数为奇数的可以使用偶数个字母
    # 只需要判断是否有一个奇数，那么最后就加一即可
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        flag = 0
        count = {}
        for i in s:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        for c in count.values():
            if c%2==0:
                res +=  c  
            else:
                res +=  c-1
                flag = 1
        if flag==1:
            return res+1
        return res
    # 2 同样使用一个list保存
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        letter = [chr(i) for i in range(ord('a'), ord('z')+1)] + [chr(j) for j in range(ord('A'), ord('Z')+1)]
        result = 0
        for i in letter:
            result += s.count(i)//2
        ind = 0
        for i in letter:
            if s.count(i)%2 == 1:
                ind = 1
                break 
        result = 2*result + ind
        return result