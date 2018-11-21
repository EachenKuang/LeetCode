# https://leetcode.com/problems/reorganize-string/description/
class Solution:
	# 1 
	# 先把字符串排成按照重复数量从大到小的顺序的
	# 例如："abbbccdddde" => "ddddbbbccae"
	# 然后将字符串分成两节插空排
	def reorganizeString(self, S):
	    a = sorted(sorted(S), key=S.count)
	    h = len(a) / 2
	    a[1::2], a[::2] = a[:h], a[h:]
	    return ''.join(a) * (a[-1:] != a[-2:-1])
