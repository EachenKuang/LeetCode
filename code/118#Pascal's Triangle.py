# https://leetcode.com/problems/pascals-triangle/description/
class Solution:
    # 1
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []
        if numRows==1:
            return [[1]]
        if numRows==2:
            return [[1],[1,1]]
        res = [[1],[1,1]]
        currentRow = 3
        while currentRow<=numRows:
            lastRowList = res[-1]
            tempList = [1]
            for i in range(len(lastRowList)-1):
                tempList.append(lastRowList[i]+lastRowList[i+1])
            tempList.append(1)
            res.append(tempList)  
            currentRow +=1
        return res
    # 2
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triag = [[0]]
        row = []
        for rsize in range(1,numRows+1):
            row = [0 for i in range(rsize)]
            row[0] = row[-1] = 1
            for i in range(1,rsize-1):
                row[i] = triag[-1][i] + triag[-1][i-1]
            triag.append(row)
        return triag[1:]