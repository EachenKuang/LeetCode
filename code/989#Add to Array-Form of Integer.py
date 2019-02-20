class Solution:
    def addToArrayForm(self, A: 'List[int]', K: 'int') -> 'List[int]':
        b = ''.join(list(map(str,A)))
        c = list(str(int(b) + K))
        return list(map(int,c))