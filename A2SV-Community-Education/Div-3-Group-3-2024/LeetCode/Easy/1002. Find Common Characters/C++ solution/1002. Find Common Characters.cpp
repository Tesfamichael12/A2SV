class Solution {
public:
    vector<string> commonChars(vector<string>& words) {
        vector <string> result;
        // It's better to use an unordered map since the Time Complexity will be O(n) unlike the normal map which has O(nlog n) for sorting, to use it we muct include <unordered_map>
        unordered_map<char, int> common_character_count;

        // Initalize common_character_count with the first string in words
        for (char ch : words[0])
            common_character_count[ch]++;

        for (int i = 1; i < words.size(); i++)
        {
            // store the current character count starting form the second string in words
            unordered_map <char, int> current_character_count;
            for (char ch : words[i])
                current_character_count[ch]++;

            // Update common_character_count to keep the minimum, this step will keep only the common character
            for (auto& pair : common_character_count)
            {
                // To be able to use the min function we must inclued algorithm
                pair.second = min (pair.second, current_character_count[pair.first]);
            }
        }

        // Append the common characters to result with respect to thier frequencies
        for (auto& pair : common_character_count)
        {
            for (int i = 0; i < pair.second; i++)
                result.push_back(string(1, pair.first));  // Convert char to string since we cannot return a vector that contain characters
        }

        return result;
    }
};