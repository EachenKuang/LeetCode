# https://leetcode.com/problems/longest-word-in-dictionary/description/
"""
Given a list of strings words representing an English Dictionary,
find the longest word in words that can be built one character at a time by other words in words.
If there is more than one possible answer, return the longest word with the smallest lexicographical order.

If there is no answer, return the empty string.
Example 1:
Input:
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation:
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
Example 2:
Input:
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation:
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically small
"""


from collections import defaultdict
class Solution(object):
    # 1
    # 使用difaultdict可以一个key映射一个list类型的value
    # 将长度相同的word装入同一个桶中
    def longestWord1(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        seen, res = set(""), ""
        buckets = defaultdict(list)
        min_len, max_len = float('inf'), float('-inf')
        for idx, w in enumerate(words):
            buckets[len(w)].append(idx)
            min_len, max_len = min(min_len, len(w)), max(max_len, len(w))
        for l in range(min_len, max_len+1):
            for idx in buckets[l]:
                w = words[idx]
                if w[:-1] in seen:
                    seen.add(w)
                    if len(w) > len(res) or (len(w) == len(res) and res > w):
                        res = w
        return res
    # 2
    # 先排序
    def longestWord2(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        max_len = 0
        ans = ""
        words.sort(key=lambda x: len(x))
        D = {}
        for w in words:
            if len(w) == 1 or w[:-1] in D:
                D[w] = 1
                if len(w) > max_len:
                    ans = w
                    max_len = len(w)
                if w < ans: ans = w
        return ans