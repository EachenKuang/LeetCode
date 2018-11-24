# https://leetcode.com/problems/sort-array-by-parity-ii/description/
class Solution:
    def sortArrayByParityII(self, A):
        odd_list = []
        even_list = []
        
        for i in A:
            if i % 2 == 1:
                odd_list.append(i)
            else:
                even_list.append(i)

        result = [None]*(len(odd_list)+len(even_list))
        result[::2] = even_list
        result[1::2] = odd_list
        return result
        
    def sortArrayByParityII(self, A):
        lastEvenPlace = 0
        lastOddPlace = 1
        result = A.copy()
        for i in A:
            if i%2 == 0:
                result[lastEvenPlace] = i
                lastEvenPlace += 2
            else:
                result[lastOddPlace] = i
                lastOddPlace += 2
        return result