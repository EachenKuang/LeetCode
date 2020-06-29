# https://leetcode.com/problems/rabbits-in-forest/description/
"""
In a forest, each rabbit has some color. Some subset of rabbits (possibly all of them) tell you how many other rabbits have the same color as them. Those answers are placed in an array.

Return the minimum number of rabbits that could be in the forest.

Examples:
Input: answers = [1, 1, 2]
Output: 5
Explanation:
The two rabbits that answered "1" could both be the same color, say red.
The rabbit than answered "2" can't be red or the answers would be inconsistent.
Say the rabbit that answered "2" was blue.
Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.

Input: answers = [10, 10, 10]
Output: 11

Input: answers = []
Output: 0
Note:

answers will have length at most 1000.
Each answers[i] will be an integer in the range [0, 999].
"""
class Solution:
    # 1
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        from collections import Counter
        mapping = Counter(answers)
        ret = 0
        for idx,val in mapping.items():
            ret += val if val%(idx+1)==0 else (val//(idx+1)+1)*(idx+1)
        return ret
    # 2
    # 用了ceil 天花板函数
    # 比1更快
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        from collections import Counter
        dic = Counter(answers)
        return sum([math.ceil(dic[i]/(i+1)) * (i+1) for i in dic.keys()])
        # return sum([(dic[i]+i) // (i+1) *(i+1) for i in dic.keys()])