class Solution {
public:
    bool isPalindrome(int x) {
    if (x < 0)
    return false;
     int div = 1;
     while (x / div >= 10)
     {
        div *= 10;
     }

     while (x)
     {
        int lsb = x % 10;
        int msb = x / div; // msb(most significant digit)
        if (lsb != msb)
        return false;
        x = (x % div) / 10; // % has more presidence than / so we may not need the ()
        div /= 100; // update div since we have eliminated two decimal places
     }
     return true;
    }
};