/* PROBLEM:
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
*/
// +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#include <iostream>
#include <vector>   // 1. include the standard c++ libarary for using vectors
using namespace std;

class Solution {
    public:
        // 3a. create a public class member function that returns a vector
        vector<int> twoSum(vector<int>& nums, int target) {

            // 3b. instantiate vector object
            vector<int> container;

            // 3c. get the size of the vector
            int size = nums.size();

            // 3d. iterate for i
            for (int i=0; i<size-1; i++)
            {
                // iterate for j
                for (int j=i+1; j<size; j++)
                {
                    // check, push back, and return...?
                    if (nums[i] + nums[j] == target)
                    {
                        // push the values into the vector and return it
                        container.push_back(i);
                        container.push_back(j);
                        return container;
                    }
                }
            }

            // 3e. default return object
            return container;
        }
};

int main()
{
    // 2a. create a vector of integers
    cout << "\nVector: ";
    vector<int> values;
    // - insert the values
    for (int i=1; i<=5; i++)
    {
        values.push_back(i);
    }
    // - display the values
    for (auto i=values.begin(); i!=values.end(); i++)
    {
        cout << *i << " ";
    }

    // 2b. create a target value to find
    int number = 9;
    cout << "\nTarget value: " << number << "\n";

    // 2c. create an object of the "Solution" class to find the answer
    Solution test;

    // 4. display correct answers
    // - create a new vector, call the member function and store it in new vector, then display the solution
    vector<int> mySolutions;
    mySolutions = test.twoSum(values, number);
    cout << "SUCCESS: index[" << mySolutions[0] << "] + index[" << mySolutions[1] << "] = " << number << endl << endl;

    return 0;
}