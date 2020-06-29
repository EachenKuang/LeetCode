# https://leetcode.com/problems/most-common-word/description/
from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        count=collections.Counter(piece for piece in re.split('[ !?\',;.]',paragraph.lower()) if piece)
        banned=set(banned)
        return max((item for item in count.items() if item[0] not in banned),key=operator.itemgetter(1))[0]

# re.split
# 函数 re.split() 是非常实用的，因为它允许你为分隔符指定多个正则模式。 
# 比如，分隔符可以是逗号，分号或者是空格，并且后面紧跟着任意个的空格。 
# 只要这个模式被找到，那么匹配的分隔符两边的实体都会被当成是结果中的元素返回。 
# 返回结果为一个字段列表，这个跟 str.split() 返回值类型是一样的。