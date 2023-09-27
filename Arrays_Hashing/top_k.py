"""
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    SUMMARY:
    - you can create a list of lists like this:
        freq = [[]];

    - you can create a list of lists with a size like this:
        freq = [[] for i in range(7)]

    - you can iterate thru a list backwards like this:
        for i in range(7, 0, -1)
        # the 7 is the size of the list
        # the 0 is the number we're going to
        # the -1 is decrementing by 1

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""

# QUESTION:
# Given an integer array nums and an integer k, return the k most frequent elements. 
# You may return the answer in any order.
class Solution(object):
    
    # 3. given an input "nums[]" and value "k", return the "k" most frequent values from the input
    def topKFrequent(self, nums, k):

        """
        *** MY VERSION ***
            # 4. sort the list from least to greatest
            nums = sorted(nums);

            # 5. create empty hashmap to organize data
            hashmap = {};

            # 6. iterate thru list, store key pairs (value -> amount_of_times_that_value_is_in_the_list)
            for index, val in enumerate(nums):
                # - the "hashmap.get(nums[index], 0)" will get the value associated with the key in "hashmap[nums[index]]"
                # - if there is no value associated with it, it will use the default value of "0"
                hashmap[nums[index]] = 1 + hashmap.get(nums[index], 0);
            
            # 7. sort the hashmap to have greatest-to-least values from the key-value pairs
            sorted_hashmap = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))

            # 8. return the top "k" amount of elements 
            # - store the top "k" amount of elements inside another list and return that
            # - sort the key-value pairs with the largest values in the key-value pairs
            count = 0;
            answer = [];
            for key in sorted_hashmap:
                if (count < k):
                    answer.append(key);
                else:
                    break;
                count += 1;
            
            return answer;
        """

        # list to hold all number of times each value from "nums" is shown
        count = {};

        # create an empty list of lists, which will be the size of the "nums[]" list plus one
        freq = [[] for i in range(len(nums) + 1)];

        # iterate thru "nums[]" and count how many times each value is shown
        for val in nums:
            count[val] = 1 + count.get(val, 0);

        # iterate thru "count[]" to get the key-value pairs, and append the appropraite value "val" into "freq[[]]"
        for val, occurences in count.items():
            # this code says "the value 'val' occurs 'occurences' number of times"
            freq[occurences].append(val);

        # create a list to hold "k" number of results
        res = [];

        # iterate thru "freq[[]]" in descending order, this is so we can get the numbers with the most occurences
        # in the "range(len(feq) - 1, 0, -1)" code:
        # - the "len(freq) - 1" gets the correct size of the "freq[]" list
        # - the 0 means we're going from "len(freq) - 1" to "0"
        # - the -1 means we're decrementing by 1
        # - **NOTE: this code allows us to iterate a list from the last index to the first index
        for i in range(len(freq) - 1, 0, -1):
            # for every "n" value with its number of occurences "i", store the "n" value into the new list "res[]"
            for n in freq[i]:
                res.append(n);
                # once the length of "res[]" equals "k", we can return those values
                if (len(res) == k):
                    return res;

if __name__ == "__main__":
    # 1. input values
    nums = [1,1,1,2,2,3,1,5,5,5,28,28,28,28,28,8,9,20,25];
    k = 3;

    # 2. get solution
    test = Solution();
    print(test.topKFrequent(nums, k));