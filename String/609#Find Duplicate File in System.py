# https://leetcode.com/problems/find-duplicate-file-in-system/description/
class Solution:
    # 1 
    #  defaultdict 可以将一个key对应多个value
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        d = defaultdict(list)
        for p in paths:
            path, *files = p.split()
            for file in files:
                content = file[file.index('(')+1:-1]
                name = file[:file.index('(')]
                d[content].append('/'.join([path,name]))
        return list(v for v in d.values() if len(v)>=2)
