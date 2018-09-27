class Solution:
	# function1
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_x = str(x)
        left = 0
        right = len(str_x)-1
        while left < right:
            if str_x[left] == str_x[right]:
                left+=1
                right-=1
            else:
                return False
        if left-right>=0:
            return True
        return False
    # function2
    def isPalindrome(self, x):
    	return str(x) == str(x)[::-1]  
