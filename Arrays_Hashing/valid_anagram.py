"""
    SUMMARY:
    - hashmaps (aka dictionaries):
        - stores key-value pairs
        - these values are NOT unique, so there will be duplicates
        - syntax:
            # initialize an empty dictionary
            hashmap = {}        
"""

class Solution(object):
    def isAnagram(self, s, t):

        # first, check if the strings are different lengths
        # if they're different lengths, they cannot be anagrams so return false
        if (len(s) != len(t)):
            print("returning false...");
            return False;

        # 1. create two empty hashmaps
        # - each character in a string is the key
        # - the number of times that character shows in the string is its value
        # - Ex) for "anagram", 'a' is the key and '3' is the value because it shows 3 times
        hashmap1 = {};
        hashmap2 = {};
  
        # 2. add key-value pairs for each hashmap
        for i in range(len(s)):
            # the "hashmap1[s[i]]" is each character in the "s" string (aka the key)
            # the "1 + hashmap1.get(s[i], 0)" is the amount of times that character in the "s" string (aka the value)
            # - the get() function gets the value from the key
            #     - first parameter is the key you want to retrieve a value from
            #     - second parameter is a default value if the key is not found in the hashmap
            #     - **if the key is found, it returns the value already associated with it
            hashmap1[s[i]] = 1 + hashmap1.get(s[i], 0);
            hashmap2[t[i]] = 1 + hashmap2.get(t[i], 0);
        
        # iterate thru each key-value pair in both hashmaps
        for j in hashmap1:
            # the "hashmap1[j]" gets the value from that current key in the hashmap
            # the "hashmap2.get(j, 0))" gets the value associated with that current key
            # - if each key's values don't match, they're NOT anagrams so return false
            if (hashmap1[j] != hashmap2.get(j, 0)):
                print("returning false...");
                return False;

        print("returning true...");
        return True;
        
        
        

if __name__ == "__main__":
    string1 = "anagramb";
    string2 = "nagarama";
    test = Solution();
    test.isAnagram(string1, string2);