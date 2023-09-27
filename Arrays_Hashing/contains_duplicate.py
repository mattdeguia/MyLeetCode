"""
    SUMMARY:
    - hashsets (aka sets):
        - store all values only once, so there cannot be any duplicates in a set
        - only stores unique keys
        - syntax:
            # initialize an empty set
            hashset = set()     
"""

class Solution(object):
    def containsDuplicate(self, nums):
        # ---------------------------------------------------------------
        # NeetCode's Version
        # - the "set()" will create a set, which is an unordered collection of unique items
        # - sets are used to store any values and to check if a specific value exists in it
        hashset = set();


        # - iterate through each "value" in the "nums" array
        for value in nums:
            # - if the value is already in the hashset, display message and return
            if (value in hashset):
                print("\nContains Duplicates!\n");
                return True;
            # - if the value is NOT already in the hashset, add the value in there
            hashset.add(value);
        
        print("\nNo Duplicates\n");
        return False;


if __name__ == "__main__":
    nums = [1, 2, 3, 4];
    test = Solution();
    test.containsDuplicate(nums);
