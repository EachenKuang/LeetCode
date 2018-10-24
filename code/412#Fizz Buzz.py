# https://leetcode.com/problems/fizz-buzz/description/
class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = list(range(1,n+1))
        for i in range(len(res)):
            if res[i]%15==0:
                res[i]="FizzBuzz"
            elif res[i]%3==0:
                res[i]="Fizz"
            elif res[i]%5==0:
                res[i]="Buzz"
            else:
                res[i]=str(res[i])
        return res