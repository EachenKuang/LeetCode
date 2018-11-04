# https://leetcode.com/problems/student-attendance-record-i/description/
class Solution:
    # 1 常规方法
    # 设计两个计数器
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count_A = count_L = 0
        length = len(s)
        for i in s:
            if i=='A':
                count_A += 1
                count_L = 0
            elif i=='L':
                count_L += 1
            else:
                count_L = 0
            if count_A>1 or count_L>2:
                return False
        return True
    # 2 使用正则
    def checkRecord(self, s):
        return False if bool(re.search(r"(L){3,}",s)) or bool(re.search(r"(A).*\1",s)) else True
            