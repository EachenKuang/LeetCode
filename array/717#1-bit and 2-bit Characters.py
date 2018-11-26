# https://leetcode.com/problems/1-bit-and-2-bit-characters/description/
class Solution:
    # 1
    # 只有0，10，1
    # 那么遇到1就移动两位，遇到0就移动一位
    # 如果最后能够遍历完，说明是true
    def isOneBitCharacter(self, bits):
        i = 0
        while i < len(bits) - 1:
            i += bits[i] + 1
        return i == len(bits) - 1
    # 2
    # 
    def isOneBitCharacter(self, bits):
        parity = bits.pop()
        while bits and bits.pop(): 
            parity ^= 1
        return parity == 0


