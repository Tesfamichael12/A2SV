class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        int n = arr.size();
        int maxval = arr[n -1];
        vector<int> new_arr(n);
        new_arr[n-1] = -1;

        for (int i = n - 2; i >= 0; i--)
        {
            maxval = max(maxval, arr[i + 1]);
            new_arr[i] = maxval;
        }

        return new_arr;
    }
};