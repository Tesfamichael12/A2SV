class Solution {
public:
    bool validMountainArray(vector<int>& arr) {
       int n = arr.size();
       int i = 0;
       // walk up
       while (i + 1 < n && arr[i] < arr[i + 1])
           i++;
        // peak cannot be the first nor the last element
        if (i == 0 || i == n - 1)
           return false;

        // walk down
        while (i + 1 < n && arr[i] > arr[i + 1])
            i++;

        return i == n - 1;
    }
};