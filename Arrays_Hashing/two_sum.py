"""
    SUMMARY:
    - hashmaps (aka dictionaries):
        - stores key-value pairs
        - these values are NOT unique, so there will be duplicates
        - syntax:
            # initialize an empty dictionary
            hashmap = {}        

    - enumerate(array):
        - used to iterate through a list/array/tuple while keeping track of the index and value
        - syntax:
            # iterate through an array
            for index, item in enumerate(array):
"""

class Solution(object):
    def twoSum(self, nums, target):
        # create empty hashmap (value -> index)
        hashmap = {};

        # iterate through hashmap, store the value and its index
        # - i holds the index, n holds the value in that index
        for i, n in enumerate(nums):

            # subtract the target from the value in the index
            diff = target - n;

            # check if the difference is already in the hashmap
            if (diff in hashmap):
                # return the indices that hold the values "diff" and "n"
                # - the "hashmap[diff]" is the first index
                # - the "i" is the other index
                return [hashmap[diff], i];
        
            # if the difference isn't in the hashmap, store the key-value pair in the hashmap
            hashmap[n] = i;

            


# main function:
if __name__ == "__main__":

    # create array of numbers
    arr = [2, 11, 7, 15];

    # create object of class
    test = Solution();

    # use method from class
    print(test.twoSum(arr, 9));