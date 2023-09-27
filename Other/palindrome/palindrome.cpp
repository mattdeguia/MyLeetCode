/* PROBLEM:
    Given an integer x, return true if x is a palindrome, and false otherwise.
*/
// +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        // pass the value into x and always convert it into a string
        string original = "";
        string reverse = "";
        original = to_string(x);
        cout << endl;
        cout << "original string: " << original << endl;

        // reverse the string
        int length = original.length();
        for (int i=length-1; i>=0; i--)
        {
            reverse = reverse + original[i];
        }
        cout << "reverse string: " << reverse << endl;
        
        // compare the original string to the reversed string
        if (original == reverse)
        {
            cout << "IS a palindrome" << endl << endl;
            return true;
        }
        else
        {
            cout << "NOT a palindrome" << endl << endl;
            return false;
        }

        return false;
    }
};

int main()
{
    // 1. instantiate object, invoke member function with test number
    Solution test;
    test.isPalindrome(-121);


    return 0;
}