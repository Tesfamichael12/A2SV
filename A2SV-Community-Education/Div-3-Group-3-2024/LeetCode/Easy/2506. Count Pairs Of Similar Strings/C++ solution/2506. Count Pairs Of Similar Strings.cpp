class Solution {
public:
    int similarPairs(vector<string>& words) {
        int count = 0;
        // brute force solution
        for (int i = 0; i < words.size(); i++) {
            for (int j = i + 1; j < words.size(); j++) {
                set<char> set1(words[i].begin(), words[i].end());
                set<char> set2(words[j].begin(), words[j].end());
                if (set1 == set2) {
                    count += 1;
                }
            }
        }
        return count;
    }
};