# https://leetcode.com/problems/sum-of-even-numbers-after-queries/
"""
We have an array A of integers, and an array queries of queries.

For the i-th query val = queries[i][0], index = queries[i][1], we add val to A[index].  Then, the answer to the i-th query is the sum of the even values of A.

(Here, the given index = queries[i][1] is a 0-based index, and each query permanently modifies the array A.)

Return the answer to all queries.  Your answer array should have answer[i] as the answer to the i-th query.



Example 1:

Input: A = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
Output: [8,6,2,4]
Explanation:
At the beginning, the array is [1,2,3,4].
After adding 1 to A[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8.
After adding -3 to A[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6.
After adding -4 to A[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2.
After adding 2 to A[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.


Note:

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
1 <= queries.length <= 10000
-10000 <= queries[i][0] <= 10000
0 <= queries[i][1] < A.length

even => even  sum + query[1]
even => oven  sum - A[query[0]]
oven => even  sum + query[1] + A[query[0]]
oven => oven  sum

"""
class Solution:
    def sumEvenAfterQueries(self, A: '[int]', queries: '[[int]]') -> '[int]':
        ret = []
        sum_of_even = sum(a for a in A if a%2==0)
        for query in queries:
            if A[query[1]]%2==0:
                if query[0]%2:
                    sum_of_even -= A[query[1]]
                else:
                    sum_of_even += query[0]
            else:
                if query[0]%2:
                    sum_of_even += query[0] + A[query[1]]
            A[query[1]] += query[0]
            ret.append(sum_of_even)
        return ret

# Runtime: 172 ms, faster than 48.73% of Python3 online submissions for Sum of Even Numbers After Queries.
# Memory Usage: 16.8 MB, less than 100.00% of Python3 online submissions for Sum of Even Numbers After Queries.
#

