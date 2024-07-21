class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {

    string longest = strs[0], shortest = strs[0];
    for (int i = 1; i < strs.size(); i++) // for vectors we cnnot use the length() mehtod 
    {
        longest = (longest > strs[i] ? longest : strs[i]);
        shortest = (shortest < strs[i] ? shortest : strs[i]);
    }
    int i; // declare it here first to use it on the outer return statement 
    for (i = 0; i < shortest.size(); i++)
    {
        if (longest[i] != shortest[i])
        return longest.substr(0, i);
    }
    return longest.substr(0, i);
    }
};