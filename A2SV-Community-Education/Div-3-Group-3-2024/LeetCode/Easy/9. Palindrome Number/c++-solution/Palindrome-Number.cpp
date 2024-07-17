class Solution {
public:
    bool isPalindrome(int x) {
    
        // if (x < 0)
        // return false; // here if we are to change x to str we don't need to check if it is -ve, the while loop will takecare of that
        //uing two pointers technique by changing int to str 
        // Time complexity = O(n) , Space complexity = O(1)
        string num = to_string(x); // in c++ we use to_stirng() method to convert int to str
        int L = 0;
        int R = num.length() - 1;
        while (L < R){
            if (num[L] != num[R])
            return false;
            L++;
            R--;
        }
        return true;
    }
};