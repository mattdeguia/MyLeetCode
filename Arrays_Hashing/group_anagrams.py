"""
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    SUMMARY:
    - the "from collections import defaultdict" allows us to create a dictionary to have whatever
      default value type we specify, otherwise its default value type will be "None"
    - the "ord()" function returns the unicode value of a single character
    - for "tuple(count)", we're converting "count[]" from a list to a tuple
    - dictionaries and hashmaps are the same, dictionaries are just python's implementation of hashmaps
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""

from collections import defaultdict;

class Solution(object):
    def groupAnagrams(self, strs):
        """
        summary:
        - strs is an array of different strings
        - find the strings that are anagrams and group them together
        - always group the string within the array, even if it's only one string
        """

        # create a list to hold groups of anagrams
        res = defaultdict(list);

        # iterate through each string in the list
        for s in strs:
            # create a list of 0's to represent each letter in the alphabet
            # count = [0, 0, 0, 0, 0, 0, ...]
            # count[0] represents "a", count[1] represents "b", and so on...
            count = [0] * 26;

            # iterate through each character in the current string
            # here, we are assigning the amount of times each letter shows in the string
            for c in s:
                # the "ord()" function returns the unicode value
                # we use this to our advantage to assign each character to its appropriate index in "count[]"
                # Ex) for "abc", it will be "count[1, 1, 1, 0, 0, 0, .....]"
                # Ex) for "cab", it will also be "count[1, 1, 1, 0, 0, 0, .....]"
                #     **NOTE: since "abc" and "cab" have the same letters, their "count[]" lists have the same values
                # Ex) for "aabc", it will be "count[2, 1, 1, 0, 0, 0, .....]"
                count[ord(c) - ord("a")] += 1;

            # now we can group the anagrams into their appropriate tuples
            # we do this by appending each strings into the tuple that has the same "count[]" values
            # **NOTE: since each "count[]" is a list, we need to convert it into a tuple so it can hold 
            #         multple values within each index. the tuple acts as a key to group each string correctly 
            # Ex) since the "abc" and "cab" strings have the same "count[]" values, which are 
            #     "count[1, 1, 1, 0, 0, 0, .....]", we need to group those strings together
            res[tuple(count)].append(s);

        # then we can return the grouped anagrams
        return res.values();

if __name__ == "__main__":

    myArray = ["eat","tea","tan","ate","nat","bat"];
    groupedArray = [];

    test = Solution();
    groupedArray = test.groupAnagrams(myArray);

    print(groupedArray);