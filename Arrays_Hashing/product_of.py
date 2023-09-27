"""
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    SUMMARY:
    - i don't even know how he came up with this solution
    - i still kinda don't get it

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""

# QUESTION:
# Given an integer array nums, return an array answer such that answer[i]
# is equal to the product of all the elements of nums except nums[i].
# Time complexity MUST be O(n)
class Solution(object):

    def productExceptSelf(self, nums):
        # create list to have all 1s
        answer = ([1] * len(nums));

        # get the prefix answers
        prefix = 1;
        for i in range(len(nums)):
            answer[i] = prefix;
            prefix = prefix * nums[i];
        
        # get the postfix answers
        postfix = 1;
        for i in range(len(nums) - 1, -1, -1):
            answer[i] = answer[i] * postfix;
            postfix = postfix * nums[i];
        
        # return the asnwer
        return answer;

        

# main function:
if __name__ == "__main__":
    nums = [1,2,3,4];
    test = Solution();
    print(test.productExceptSelf(nums));