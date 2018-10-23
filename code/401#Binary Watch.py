# https://leetcode.com/problems/binary-watch/description/
class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """       
        return ['%d:%02d' % (h, m)
                for h in range(12) for m in range(60)
                if (bin(h) + bin(m)).count('1') == num]


h = [['0'], ['1', '2', '4', '8'], ['3', '5', '6', '9', '10'], ['7', '11']]
m = [['00'], 
     ['01', '02', '04', '08', '16', '32'], 
     ['03', '05', '06', '09', '10', '12', '17', '18', '20', '24', '33', '34', '36', '40', '48'],
     ['07', '11', '13', '14', '19', '21', '22', '25', '26', '28', '35', '37', '38', '41', '42', '44', '49', '50', '52', '56'],
     ['15', '23', '27', '29', '30', '39', '43', '45', '46', '51', '53', '54', '57', '58'],
     ['31', '47', '55', '59']]

class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        ans = []
        for i in range(max(0, num - 5), min(num + 1, 4)):
            ans += [x + ':' + y for x in h[i] for y in m[num - i]]
        return ans