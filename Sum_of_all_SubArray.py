
"""
You are given an integer array A of length N.
You have to find the sum of all subarray sums of A.

PS: A subarray sum denotes the sum of all the elements of that subarray.
"""
class Solution:
    """
    Naive approach: Calculate every subarray sum , it leads to O(n^3)
    Optimised approach : Calculate the Contribution of each element of array
    to the subarray sums based on its position : O(N)

    """
    def Sum_of_all_SubArray(self,array):
        Sum=0
        n=len(array)
        for i in range(n):
            # multiple how many times it repeated in subarray  with Current Value
            Sum+= array[i]*(i+1)*(n-i) # formula ->(i+1)*(n-i) with array element
        return Sum
if __name__ == '__main__':
    array=list(map(int,input().split()))
    print(Solution().Sum_of_all_SubArray(array))

