# First of all, it is easy to argue that starting from a number I, if some value - say a - appears again during the process after k steps, the initial number I cannot be a happy number. Because a will continuously become a after every k steps.

# Therefore, as long as we can show that there is a loop after running the process continuously, the number is not a happy number.

# There is another detail not clarified yet: For any non-happy number, will it definitely end up with a loop during the process? This is important, because it is possible for a non-happy number to follow the process endlessly while having no loop.

# To show that a non-happy number will definitely generate a loop, we only need to show that for any non-happy number, all outcomes during the process are bounded by some large but finite integer N. If all outcomes can only be in a finite set (2,N], and since there are infinitely many outcomes for a non-happy number, there has to be at least one duplicate, meaning a loop!

# Suppose after a couple of processes, we end up with a large outcome O1 with D digits where D is kind of large, say D>=4, i.e., O1 > 999 (If we cannot even reach such a large outcome, it means all outcomes are bounded by 999 ==> loop exists). We can easily see that after processing O1, the new outcome O2 can be at most 9^2*D < 100D, meaning that O2 can have at most 2+d(D) digits, where d(D) is the number of digits D have. It is obvious that 2+d(D) < D. We can further argue that O1 is the maximum (or boundary) of all outcomes afterwards. This can be shown by contradictory: Suppose after some steps, we reach another large number O3 > O1. This means we process on some number W <= 999 that yields O3. However, this cannot happen because the outcome of W can be at most 9^2*3 < 300 < O1.

# https://leetcode.com/problems/happy-number/description/
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def calculateSum(n):
            sum = 0
            while(n):
                tmp = n % 10
                sum += tmp * tmp
                n //= 10
            return sum;
        
        slow = fast = n;
        while True:
            slow = calculateSum(slow);
            fast = calculateSum(fast);
            fast = calculateSum(fast);
            if slow==fast:
                break
        if slow == 1:
            return True
        else:
            return False;