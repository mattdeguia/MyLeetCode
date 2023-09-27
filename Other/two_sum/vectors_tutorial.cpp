/* TASKS:
    - learn how to use vectors
    - learn how to use vectors in a class
*/

/* MY NOTES:
    - you can treat the vector as a regular array when accessing values in it
*/
#include <iostream>
#include <vector>

using namespace std;

int main()
{

    // 1a. instantiate a vector object that holds integers
    vector<int> g1;
    cout << "\n";

    // 1b. push values into the vector
    cout << "Inserting values into vector..." << endl;
    for (int i=1; i<=5; i++)
    {
        g1.push_back(i);
    }
    cout << "\n\n";


    // 2a. output all files with begin() and end()
    // - The "auto" keyword automatically determines what datatype "i" will be
    // - The begin() function returns the value from the beginning of the vector
    cout << "Display values from start of vector: " << endl;
    for (auto i=g1.begin(); i!=g1.end(); ++i)
        cout << *i << " ";
    cout << "\n\n";

    // 2b. output all files with rbegin() and rend()
    // - The rbegin() function returns the value from the end of the vector
    cout << "Display all values from end of vector: " << endl;
    for (auto i=g1.rbegin(); i!=g1.rend(); i++)
        cout << *i << " ";
    cout << "\n\n";

    // 3a. output all files with cbegin() and cend()
    // Displays all values from start to end of vector, where values are constant
    // - The cbegin() function returns the constant value from the beginning of the vector
    cout << "Display all constant values from start of vector: " << endl;
    for (auto i=g1.cbegin(); i!=g1.cend(); i++)
        cout << *i << " ";
    cout << "\n\n";

    // 3b. output all files with crbegin() and crend()
    // Displays all values from end to start of vector, where values are constant
    // - The crbegin() function returns the constant value from the end of the vector
    cout << "Display all constant values from end of vector: " << endl;
    for (auto i=g1.crbegin(); i!=g1.crend(); i++)
        cout << *i << " ";
    cout << "\n\n";

    // 4. accessing values in the vector
    cout << "displaying first element in vector: ";
    cout << g1[0] << endl;
    cout << "displaying last element in vector: ";
    cout << g1[4] << endl;
    cout << "\n\n";


    return 0;
}