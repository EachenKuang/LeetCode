# Given an array of strings, group anagrams together.
#
# Example:
#
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:
#
# All inputs will be in lowercase.
# The order of your output does not matter.
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        res_dict = defaultdict(list)
        for s in strs:
            k = ''.join(sorted(s))
            res_dict[k].append(s)
        return list(res_dict.values())

    # def groupAnagrams1(self, strs):
    #     ans = defaultdict()
    #     for s in strs:
    #         count = [0] * 26
    #         for c in s:
    #             count[ord(c) - ord('a')] += 1
    #         ans[tuple(count)].append(s)
    #     return ans.values()
if __name__ == '__main__':
    after = [
      ["ate","eat","tea"],
      ["nat","tan"],
      ["bat"]
    ]
    before = ["eat", "tea", "tan", "ate", "nat", "bat"]
    solution = Solution()
    print(solution.groupAnagrams(before))
    assert after == solution.groupAnagrams(before)
