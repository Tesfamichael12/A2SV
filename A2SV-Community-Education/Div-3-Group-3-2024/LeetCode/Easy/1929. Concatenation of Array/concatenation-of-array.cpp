class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        // Time Complexity : O(N) insert opration
       nums.insert(nums.end(), nums.begin(), nums.end());
       return nums;

       // or using one for loop and the push_back method
    }
};